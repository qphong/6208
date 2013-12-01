from rockSample import *
from rSmdpSolver import *
from random import *
from time import *
import rsMDPSlvi as mdpSlvi

discount_fac=0.95

# discount_factor for RockSample(7,8)
dis_RB=0.00012

def makePolicyDict(rs_Mmdp, policyList):

	policy = {}
	for i in range( len(rs_Mmdp.states) ):
		policy[rs_Mmdp.states[i]] = policyList[i]

	return policy

mdp_numStates = 0
mapStates = {}
mdp_trans_act = []
mdp_trans_nxtS = []
mdp_trans_p = []
mdp_rewards = []
mdp_rb = []

def initIndexingModel(rs_Mmdp):

	global mdp_numStates
	global mapStates
	global mdp_trans_act
	global mdp_trans_nxtS
	global mdp_trans_p
	global mdp_rewards
	global mdp_rb

	mdp_numStates = len(rs_Mmdp.states)

	c = 0
	mapStates = {}
	for s in rs_Mmdp.states:
		mapStates[s] = c
		c += 1	

	tmp = []
	for i in range(c):
		tmp.append( mdpSlvi.vec1s(rs_Mmdp.adj[ rs_Mmdp.states[i] ].keys()) )
	mdp_trans_act = mdpSlvi.vec2s(tmp)
	
	tmp = []
	for i in range(c):
		tmp1 = []
		s = rs_Mmdp.states[i]
		for a in rs_Mmdp.adj[s]:
			tmp2 = []
			for nxtS in rs_Mmdp.adj[s][a]:
				tmp2.append( mapStates[nxtS] )
			tmp1.append( mdpSlvi.vec1i(tmp2) )
		tmp.append( mdpSlvi.vec2i(tmp1) )
	mdp_trans_nxtS = mdpSlvi.vec3i(tmp)

	mdp_trans_p = []
	for i in range(c):
		tmp1 = []
		s = rs_Mmdp.states[i]
		for a in rs_Mmdp.adj[s]:
			tmp2 = []
			for nxtS in rs_Mmdp.adj[s][a]:
				tmp2.append( 0.0 )
			tmp1.append( tmp2 )
		mdp_trans_p.append( tmp1 ) 

	mdp_rewards = []
	for i in range(c):
		tmp1 = []
		s = rs_Mmdp.states[i]
		for a in rs_Mmdp.adj[s]:
			tmp1.append( 0.0 )
		mdp_rewards.append( tmp1 )

	mdp_rb = []
	for i in range(c):
		tmp1 = []
		s = rs_Mmdp.states[i]
		for a in rs_Mmdp.adj[s]:
			tmp1.append( 0.0 )
		mdp_rb.append( tmp1 )


def makeIndexingModel(rs_Mmdp):

	global mdp_numStates
	global mapStates
	global mdp_trans_act
	global mdp_trans_nxtS
	global mdp_trans_p
	global mdp_rewards
	global mdp_rb

	for i in range(mdp_numStates):
		s = rs_Mmdp.states[i]
		tmpA = 0
		for a in rs_Mmdp.adj[s]:
			tmpN = 0
			for nxtS in rs_Mmdp.adj[s][a]:
				mdp_trans_p[i][tmpA][tmpN] = rs_Mmdp.trans[s][a][nxtS]
				tmpN += 1
			tmpA += 1

	for i in range(mdp_numStates):
		s = rs_Mmdp.states[i]
		tmpA = 0
		for a in rs_Mmdp.adj[s]:
			mdp_rewards[i][tmpA] = rs_Mmdp.rewards[s][a]
			tmpA += 1

	for i in range(mdp_numStates):
		s = rs_Mmdp.states[i]
		tmpA = 0
		for a in rs_Mmdp.adj[s]:
			mdp_rb[i][tmpA] = rs_Mmdp.RB[s][a]
			tmpA += 1


def Simulation(rs_Mmdp):

	global mdp_numStates
	global mapStates
	global mdp_trans_act
	global mdp_trans_nxtS
	global mdp_trans_p
	global mdp_rewards
	global mdp_rb

	#accumulate reward
	acc_reward=0

	#discount of the RB
	flag=1

	m_policy={}

	init_horizon=rs_Mmdp.H

	d_fac = discount_fac
	for i in range(init_horizon):
		print "i:", i
		if flag==1:
			rs_Mmdp.calTrans()
			rs_Mmdp.calRewards()
			rs_Mmdp.calRB()

		curTime = clock()
		# # Python code
		m_policy = RS_mdp_solver(rs_Mmdp,dis_RB,discount_fac)
		print "Python solver", (clock() - curTime), "seconds"
		curTime = clock()

		# C++ code
		makeIndexingModel(rs_Mmdp)
		mdp_trans_pVec = mdpSlvi.vec3d(mdp_trans_p)
		mdp_rewardsVec = mdpSlvi.vec2d(mdp_rewards)
		mdp_rbVec = mdpSlvi.vec2d(mdp_rb)
		
		print "Make model:", (clock() - curTime), "seconds"
		curTime = clock()

		policyList = mdpSlvi.RS_mdp_solver(mdp_numStates, mdp_trans_act, \
			mdp_trans_nxtS, mdp_trans_pVec, mdp_rewardsVec,\
			mdp_rbVec, \
			rs_Mmdp.H, dis_RB, discount_fac)

		m_policy = makePolicyDict(rs_Mmdp, policyList)

		print "C++ solver", (clock() - curTime), "seconds"
		# # test implementation Python and C++
		# for s in rs_Mmdp.states:
		# 	if m_policy[s] != m_policy1[s]:
		# 		print s, m_policy[s], m_policy1[s]
		# print "finish test"

		#execute part
		[flag,reward]=rs_Mmdp.execution(m_policy)
		#print reward
		acc_reward+=reward*d_fac
		#print acc_reward
		d_fac *= discount_fac

		if rs_Mmdp.cur_state=='s,'+ '0,' +str(rs_Mmdp.GridDimension):
			break

	return acc_reward


# def genRocks():

# 	rocks = []
# 	for i in range(8):
# 		r = random()
# 		if r > 0.5:
# 			rocks.append('g')
# 		else:
# 			rocks.append('b')
# 	return rocks

def genRocks(i, num_r):
	# i: 0 -> 2^8 - 1

	rocks = ['b'] * num_r
	for j in range(num_r):
		if i & (1 << j) != 0:
			rocks[j] = 'g'

	return rocks


def main():

	#############################
	#############################
	#number of rocks
	Num_rocks=11
	#############################
	#############################

	#curTime = clock()

	print "dis_RB =", dis_RB


	avgReward = 0.0

	for i in range(1):
		for j in range(2**11):
			rocks = genRocks(j, Num_rocks)
			print rocks
			rs_Mmdp=MDP(rocks)
			initIndexingModel(rs_Mmdp)
			rw = Simulation(rs_Mmdp)
			print rw
			avgReward += rw / 2048.0

	print avgReward
	# rs_Mmdp=MDP()
	# rw =Simulation(rs_Mmdp)

	# print rw


	#print (clock() - curTime), 'seconds'


if __name__=="__main__":
	main()
