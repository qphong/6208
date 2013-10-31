import numpy as np

def mdp_solver(states, action, trans_s1, trans_p, reward, rb, re, discount_fac):
	#initilize the parameters

	discount_fac = 0.99

	val = [np.zeros(len(states)), np.zeros(len(states))]
	cur = 0
	policy=np.zeros(len(states),np.int8)
	
	noChange=0

	count = 0
	while noChange==0:

		cur = 1 - cur
		noChange=1

		for i in range(len(states)):
			s=states[i]
			a=policy[states[i]]
			temp_futu_v=0
			for j in range(len(trans_s1[s][a])):
				temp_futu_v+=trans_p[s][a][j]*val[1 - cur][trans_s1[s][a][j]]
			val[cur][s]=reward[s][a]+rb[s][a]+re[s][a]+discount_fac*temp_futu_v

		# print val[cur]

		cur = 1 - cur

		for s in states:
			Qbest=val[1 - cur][s]
			for a in action:
				temp_fv=0
				for j in range(len(trans_s1[s][a])):
					temp_fv+=trans_p[s][a][j]*val[1 - cur][trans_s1[s][a][j]]
				Qsa=reward[s][a]+rb[s][a]+re[s][a]+discount_fac*temp_fv
				
				if(Qsa>Qbest):
					#print Qsa, Qbest
					policy[s]=a
					val[cur][s]=Qsa
					noChange=0

		# print count, val[cur]
		# print count, policy

		count += 1

	return [policy, val[cur]]
					
				
