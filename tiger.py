#this file describes the model of tiger
# you can get the state, action space, observation space; get the belief over MDPs; update the belief, get the transition, observation funciton, e.t.c.

import envir
import numpy as np
import random as ran

class tiger_envir(envir.static_envir):
	# basic elment

	# functionss
	def __init__(self):
		self.states=np.array([0,1])     # start, end
		self.actions=np.array([0,1,2])  # 0-LS  1-OL  2-OR
		self.num_mdps=2
		self.belief=np.array([0.5,0.5])
		self.obs=np.array([0,1])    #0-TL 1-TR	
		self.true_model=0
		#trans=np.array([[[1,0],[0,1],[0,1]]])
		#obs_func=np.array([[[[0.85,0.15],[0,0],[0,0]]]],[[[[0.15,0.85],[0,0],[0,0]]]])	
			

	def  get_transitions(self,s,a):
		if s==self.states[0] and a==self.actions[0]:
			return self.states[0]
		elif s==self.states[0] and a==self.actions[1]:
			return self.states[1]
		elif s==self.states[0] and a==self.actions[2]:
			return self.states[1]

	def get_obs_func(self,s1,a,i_m,o_j):
		if i_m==0 and s1==self.states[0] and a==self.actions[0] and o_j==self.obs[0]:
			return 0.85
		elif i_m==0 and s1==self.states[0] and a==self.actions[0] and o_j==self.obs[1]:
			return 0.15
		elif i_m==1 and s1==self.states[0] and a==self.actions[0] and o_j==self.obs[0]:
			return 0.15
		elif i_m==1 and s1==self.states[0] and a==self.actions[0] and o_j==self.obs[1]:
			return 0.85
		else:
			return 1

	def get_reward(self,s,a,i_m):
		if a==self.actions[0]:
			return -1
		elif i_m==0:
			if a==self.actions[1]:
				return -100
			else:
				return 10
		else:
			if a==self.actions[1]:
				return 10
			else:
				return -100

	def execution_onestep(self, state, action):
		if action > 0: # open left or open right
			return [self.states[1]]
		else:
			temp=ran.random()
			if temp<0.85:
				return [state, self.true_model]
			else:
				return [state, 1-self.true_model]

	def update_belief(self, bel, o_i):
		
		bel2 = []

		if o_i==self.obs[0]:
			temp=bel[0]*0.85+bel[1]*0.15
			bel2 =[bel[0]*0.85/temp,bel[1]*0.15/temp]
		else:
			temp=bel[0]*0.15+bel[1]*0.85
			bel2=[bel[0]*0.15/temp,bel[1]*0.85/temp]
		
		return bel2

	def get_init_pos(self):
		return 0
			
