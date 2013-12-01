import numpy as np
from time import *

def RS_mdp_solver(rs_Mmdp, dis_RB, discount_fac):
	#states, action, trans_s1, trans_p, reward, rb, re, discount_fac):
	#initilize the parameters
	#curTime = clock()

	states = rs_Mmdp.states
	action = rs_Mmdp.actions
	trans_s1 = rs_Mmdp.adj
	trans_p = rs_Mmdp.trans
	reward = rs_Mmdp.rewards
	rb = rs_Mmdp.RB

	#print rb[rs_Mmdp.cur_state]

	val1 = {}
	val2={}
	policy = {}

	for s in states:
		val1[s]= val2[s] = 0.0
		policy[s] = 'e'

	# value iteration

	#if rs_Mmdp.H<6:
	#print rb['s63']

	for i in range(rs_Mmdp.H):
		#print val1['s30']


		for s in states:
		
			
			max_val_s=-9999

			for a in trans_s1[s]:

				tmp_futu_v = 0.0	
				for nxtS in trans_s1[s][a]:
					tmp_futu_v += trans_p[s][a][nxtS] * val1[nxtS]
				
				tmpVal = reward[s][a] + dis_RB * rb[s][a] + tmp_futu_v * discount_fac

				if tmpVal>max_val_s:
					policy[s]=a
					max_val_s=tmpVal
			val2[s]=max_val_s
		
		for s in states:
			val1[s] = val2[s]

	#print (clock() - curTime), 'seconds'

	return policy

	# policy iteration
	# noChange = 0

	# while noChange == 0:

	# 	noChange = 1

	# 	for s in states:
	# 		tmp_futu_v = 0.0
	# 		a = policy[s]
	# 		if a in trans_s1[s]:
	# 			for nxtS in trans_s1[s][a]:
	# 				tmp_futu_v += trans_p[s][a][nxtS] * val_improv[nxtS]
	# 			val_eval[s] = reward[s][a] + dis_RB * rb[s][a] + tmp_futu_v

	# 	for s in states:
	# 		Qbest = val_eval[s]
	# 		for a in trans_s1[s]:
	# 			temp_fv = 0.0
	# 			for nxtS in trans_s1[s][a]:
	# 				temp_fv += trans_p[s][a][nxtS] * val_eval[nxtS]
	# 			Qsa = reward[s][a] + dis_RB * rb[s][a] + temp_fv

	# 			if Qsa > Qbest:
	# 				policy[s] = a
	# 				val_improv[s] = Qsa
	# 				noChange = 0

	# return policy




	# val = [np.zeros(len(states)), np.zeros(len(states))]
	# cur = 0
	# policy=np.zeros(len(states),np.int8)
	
	# noChange=0

	# count = 0
	# while noChange==0:

	# 	cur = 1 - cur
	# 	noChange=1

	# 	for i in range(len(states)):
	# 		s=states[i]
	# 		a=policy[states[i]]
	# 		temp_futu_v=0
	# 		for j in range(len(trans_s1[s][a])):
	# 			temp_futu_v+=trans_p[s][a][j]*val[1 - cur][trans_s1[s][a][j]]
	# 		val[cur][s]=reward[s][a]+rb[s][a]+re[s][a]+discount_fac*temp_futu_v

	# 	# print val[cur]

	# 	cur = 1 - cur

	# 	for s in states:
	# 		Qbest=val[1 - cur][s]
	# 		for a in action:
	# 			temp_fv=0
	# 			for j in range(len(trans_s1[s][a])):
	# 				temp_fv+=trans_p[s][a][j]*val[1 - cur][trans_s1[s][a][j]]
	# 			Qsa=reward[s][a]+rb[s][a]+re[s][a]+discount_fac*temp_fv
				
	# 			if(Qsa>Qbest):
	# 				#print Qsa, Qbest
	# 				policy[s]=a
	# 				val[cur][s]=Qsa
	# 				noChange=0

	# 	# print count, val[cur]
	# 	# print count, policy

	# 	count += 1

	# return [policy, val[cur]]
					
				
