# this file is an father class of the envir, offer same shared variables and funcitons

import numpy as np

class static_envir:
	# basic elements
	states=np.array([])
	actions=np.array([])
	num_mdps=0
	belief=np.array([])
	obs=np.array([])
	#trans=np.array([[[]]])  #s,a,s1
	#obs_func=np.array([[[[]]]])  #i_m,s1,a,o_i
	#reward=np.array([[[]]])  #i_m,s1,a

	# init func
	def __init__(self):
		pass
	
	# functions
	def get_states(self):
		return self.states
	
	def get_actions(self):
		return self.actions
	
	def get_num_mdps(self):
		return self.num_mdps
	
	def get_observations(self):
		return self.obs

	def get_belief(self):
		return self.belief

