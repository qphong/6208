
"""
getNumMDPs()
getBelief()
getState()
getAct()
getObsr()
* getInitPos()
* getDestTrans(s, a) -> dest state
getObsrProb(s, a, mdlIdx, o)
getReward(s, a, mdlIdx)

? get real reward, real observation, real destination

"""

from tiger import *
from math import *
from mdp import *

# constants 
theta = 0.01 # Theorem 1: Variance based paper -> controlling ro
discount = 0.95 # Discount factor in MDP, use for reward bonus coefficient
H = 10 # planning horizon
R_MAX = 10 # maximum reward

tiger = tiger_envir()

getDestTrans = tiger.get_transitions
getObsrProb = tiger.get_obs_func
getReward = tiger.get_reward
updateBelief = tiger.update_belief
getState = tiger.get_states
getAct = tiger.get_actions
getNumMDPs = tiger.get_num_mdps
getObsr = tiger.get_observations
getBelief = tiger.get_belief
getInitPos = tiger.get_init_pos

numMDPs = getNumMDPs()

# bel = getBelief()
bel = [0.04, 0.96]

states = getState()
acts = getAct()
obsr = getObsr()

pos = [getInitPos()]

# every MDP has the same set of states
mdpStates = [ [states[0]] ]

for j in range(0, len(states) - 1): # except end state
	for k in range(0, len(obsr)):
		mdpStates.append( (states[j], obsr[k]) )

mdpStates.append([ states[len(states) - 1] ]) # end state

endState = states[len(states) - 1]


# MDP adjacency list
mdpAdjList = []

for i in range(0, len(mdpStates) - 1): # except end state
	
	mdpAdjList.append([])
	for j in range(0, len(acts)):

		mdpAdjList[i].append([])
		d = getDestTrans(mdpStates[i][0], acts[j])
		if d != endState:
		    for k in range(0, len(obsr)):
		        mdpAdjList[i][j].append([d,obsr[k]])
		else:
		    mdpAdjList[i][j].append([d])

mdpAdjList.append([])
for j in range(0, len(acts)): # end state leading to no where
    mdpAdjList[ len(mdpAdjList) - 1 ] = [[]] * len(acts)


# MDP transition function
mdpTrans = []
# index: [mdlIdx][state][action][adjancy list idx of destined state]
# map from state, action -> list of probabilities for destination states

for mdlIdx in range(0, numMDPs):

	mdpTrans.append([])
	for i in range(0, len(mdpStates)):

		mdpTrans[mdlIdx].append([])
		for j in range(0, len(acts)):

			mdpTrans[mdlIdx][i].append( [] )
			for k in range(0, len(mdpAdjList[i][j])):

				state = mdpAdjList[i][j][k]
				if len(state) > 1: # compound state

					o = state[1]
					mdpTrans[mdlIdx][i][j].append( \
					  getObsrProb(mdpStates[i][0], state[0], mdlIdx, o) )
				else:
					mdpTrans[mdlIdx][i][j].append(1.0) 

			if len(mdpAdjList[i][j]) == 0:
				mdpTrans[mdlIdx][i][j].append(0.0)


# MDP reward function
mdpReward = []

for mdlIdx in range(0, numMDPs):

	mdpReward.append([])
	for i in range(0, len(mdpStates) - 1):

		mdpReward[mdlIdx].append([])
		for j in range(0, len(acts)):
			mdpReward[mdlIdx][i].append( getReward(mdpStates[i], acts[j], mdlIdx) )

	mdpReward[mdlIdx].append([])
	for j in range(0, len(acts)):
		mdpReward[mdlIdx][ len(mdpStates) - 1 ].append(0.0) # no reward for any action in end state


def calRB_RE(s, a):
# REQUIRE: state s (ORIGINAL state), action a
# reward bonus by sum of variance of transition function
#              and sum of variance of reward function
#              w.r.t the belief

# ? should we calculate with mdpStates -> repeated reward function, since it is
# irrelevant to the observation
# the following assuming NO repeated
	
	RB = 0.0
	RE = 0.0

	if s == len(states) - 1: # end state
		
		return [0.0, 0.0] # end state


	tVar = 0.0 # variance of transition

	for k in range(0, len(obsr)):

		E2 = 0.0
		E = 0.0

		for mdlIdx in range(0, numMDPs):
			transF = getObsrProb(s, a, mdlIdx, obsr[k])
			E2 += bel[mdlIdx] * transF * transF
			E += bel[mdlIdx] * transF

		tVar += E2 - E * E

	if s == 0 and a == 0:
		print tVar, E2, E

	rVar = 0.0 # variance of reward
	E2 = 0.0
	E = 0.0
	maxReward = - 1000000000.0

	for mdlIdx in range(0, numMDPs):
	
		reF = getReward(s, a, mdlIdx)
		maxReward = max(maxReward, reF)
		
		E2 += bel[mdlIdx] * reF * reF
		E += bel[mdlIdx] * reF

	rVar += E2 - E * E


	ro = theta / (2 * (len(mdpStates)**2) * (len(acts)**2))

	rVarCoeff = 1 / sqrt(ro)
	tVarCoeff = 1 / sqrt(ro) * discount * len(mdpStates) / (1 - discount)

	RB = (rVarCoeff * rVar + tVarCoeff * sqrt(tVar)) / 1000
	RE = - (maxReward - E)

	return [RB, RE]


def compoundToSingleIdx(cS):
	# INPUT: compound state cS
	# REQUIRES: end state is the largest index (len(states) - 1)
	#           starting state is the smallest index (0)

	if len(cS) == 1:
		if cS[0] == 0:
			return 0
		else:
			return cS[0] * len(obsr) + 1
	else:
		return cS[0] * len(obsr) + cS[1] + 1


def singleToCompoundIdx(sS):
	# INPUT: single state MDP
	# OUTPUT: compound state (physical state, observation)

	if sS == 0:
		return [0] # starting state
	if sS == len(mdpStates) - 1:
		return [ (sS - 1) / len(obsr) ] # end state
	else:
		return [(sS - 1) / len(obsr), (sS - 1) % len(obsr)]


def getMdpStates():

	mdpSState = []

	for s in mdpStates:
		mdpSState.append( compoundToSingleIdx(s) )

	return mdpSState


def getMdpActs():

	return acts


def getMdpAdj():
    # convert mdpAdjList to new adjList with single state representation 
    # for compound states
    # map from state, action -> list of destination states

	adjL = []

	adjL.append([])
	for i in range(len(acts)):

		adjL[0].append([])
		for j in range(len(mdpAdjList[0][i])):
			adjL[0][i].append( compoundToSingleIdx(mdpAdjList[0][i][j]) )


	for i in range(1,len(mdpStates) - 1):

		adjL.append([])
		for j in range(len(acts)):
			
			adjL[i].append([])
			for k in range(len(mdpAdjList[ mdpStates[i][0] ][j])):
				adjL[i][j].append( compoundToSingleIdx(mdpAdjList[ mdpStates[i][0] ][j][k]) )

	adjL.append([])
	adjL[ len(adjL) - 1 ] = [[ len(adjL) - 1 ]] * len(acts)

	return adjL


# mdpTrans and mdpReward are the same
def getMdpTrans(belief):
# mean transition over the belief

	trans = []
	for i in range(0, len(mdpStates)):

		trans.append([])
		for j in range(0, len(acts)):

			trans[i].append([])

			for k in range(0, len( mdpAdjList[i][j] )):

				expectTrans = 0.0

				for mdlIdx in range(0, numMDPs):
					expectTrans += mdpTrans[mdlIdx][i][j][k] * belief[mdlIdx]

				trans[i][j].append(expectTrans)

			if len( mdpAdjList[i][j] ) == 0:
				trans[i][j].append(0.0)

	return trans


def getMdpRewards(belief):
# mean rewards over the belief

	rewards = []
	for i in range(0, len(mdpStates)):

		rewards.append([])
		for j in range(0, len(acts)):

			expectRe = 0.0

			for mdlIdx in range(0, numMDPs):
				expectRe += mdpReward[mdlIdx][i][j] * belief[mdlIdx]

			rewards[i].append(expectRe)

	return rewards


def getRB_RE_list(rbCoeff = 1.0, reCoeff = 1.0):
	# return list of reward bonus
	#        and list of reward regret
	#        for all states (single number representation)
	#                and actions

	rBonus = []
	rRegret = []

	for i in range(0, len(mdpStates)):

		rBonus.append([])
		rRegret.append([])

		for j in range(0, len(acts)):

			[rb, re] = calRB_RE(mdpStates[i][0], acts[j])

			rBonus[i].append(rbCoeff * rb)
			rRegret[i].append(reCoeff * re)

	return [rBonus, rRegret]


# MDP setup
mStates = getMdpStates()
mActs = getMdpActs()
mAdj = getMdpAdj()

def RB_beb(s,a, mTrans, mRewards):

	shouldUpdateBel = False
	for i in mAdj[s][a]:
		
		nextS = singleToCompoundIdx( i )
		
		if len(nextS) > 1: # has observation
			shouldUpdateBel = True
			break

	if not shouldUpdateBel:
		return 0.0


	# expected maximum changes to the reward function
	mRe = 0.0
	for nextSId in range(0, len(mAdj[s][a]) ):

		maxV = 0.0
		nextCompoundS = singleToCompoundIdx( mAdj[s][a][nextSId] )
	
		if len(nextCompoundS) > 1:

			nextBel = tiger.update_belief(bel, nextCompoundS[1])
			nextMeanRe = getMdpRewards(nextBel)

			for s2 in mStates:
				for a1 in mActs:
					maxV = max(maxV, nextMeanRe[s2][a1] - mRewards[s2][a1])

			mRe += maxV * mTrans[s][a][nextSId]


	# expected maximum changes to the transition furnctions
	mTr = 0.0
	for nextSId in range(0, len(mAdj[s][a]) ):

		maxV = 0.0
		nextCompoundS = singleToCompoundIdx( mAdj[s][a][nextSId] )

		if len(nextCompoundS) > 1:

			nextBel = tiger.update_belief(bel, nextCompoundS[1])
			nextMeanTr = getMdpTrans(nextBel)

			for s2 in mStates:
				for a1 in mActs:

					sumTr = 0.0
					for i in range( 0, len(mAdj[s2][a1]) ) :
						sumTr += abs( nextMeanTr[s2][a1][i] - mTrans[s2][a1][i] )
			
					maxV = max(maxV, sumTr)

			mTr += maxV * mTrans[s][a][nextSId]

	return H * mRe + R_MAX * H**2 * mTr


def getRB_BEB_list(mTrans, mRewards):

	rbList = []

	for s in mStates:

		rbList.append([])
		for a in mActs:
			rbList[s].append( RB_beb(s, a, mTrans, mRewards) )

	return rbList

# def mdp_solver(states, action, trans_s1, trans_p, reward, rb, re, discount_fac):
while(pos[0] != endState):

	# Variance - based
	# [rb, re] = getRB_RE_list(1.0, 100.0)
	# result = mdp_solver(mStates, mActs, mAdj, getMdpTrans(bel), \
	# 	getMdpRewards(bel), rb, re, discount)
	
	# BEB
	mTrans = getMdpTrans(bel)
	mRewards = getMdpRewards(bel)

	rb = getRB_BEB_list(mTrans, mRewards)
	zero_RE = [ [0.0] * len(mActs) ] * len(mStates)
	result = mdp_solver(mStates, mActs, mAdj, mTrans, \
		mRewards, rb, zero_RE, discount)
	

	policy = result[0]
	print policy

	pos = tiger.execution_onestep(pos[0], policy[compoundToSingleIdx(pos)])

	if pos[0] == endState: # Game over!
		break

	bel = tiger.update_belief(bel, pos[1])
	print 'pos', pos
	print bel
	

