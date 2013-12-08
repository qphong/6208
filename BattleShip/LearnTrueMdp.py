from math import *

from random import *

class Battle_Ship():

	Sample_Size = 200

	GridSize = 10

	bel = [1.0/Sample_Size] * Sample_Size

	# observation vector: remember all the observations we have
	# initialized as 2 
	obs = [[2 for x in xrange(10)] for x in xrange(10)]

	# the samples
	sample_Mdps=[]

	# planning Horizon
	H = 80

	# The steps already be taken
	taken_steps=0

	# discount of RB
	dis_RB = 0.000005

	#################################
	# here we define the reward of uncorver a "1" to be 10, different from the origion model,
	# But we can still compare with them, because we can compare the success rate, once we successfully
	# find all the ship cells, then we receive the reward: 100 - num_steps, num_steps is the number of steps
	# it takes to find all the ship cells.
	#################################

	R_max=20
	R_min=-1


	## here we define the true model
	## It is represented by a 2-dimensional matrix
	true_Model =  [[2 for x in xrange(10)] for x in xrange(10)]

	# Check whether the ship satisfies the constraints
	def CheckConflict(self,x,y,dir,len):
		if dir == 0:
			l_y = y-1
			if l_y < 0:
				l_y = y
			r_y = y + len + 1
			if r_y >= self.GridSize:
				r_y = y+len
			u_x = x-1
			if u_x < 0:
				u_x = x
			d_x = x+1
			if d_x >= self.GridSize:
				d_x = x

			for i in range(u_x, d_x+1):
				for j in range(l_y,r_y+1):
					if self.true_Model[i][j] != 2:
						return False
			return True

		else:
			u_x = x-1
			if u_x < 0:
				u_x = x
			d_x = x + len + 1
			if d_x >= self.GridSize:
				d_x = x +len
			l_y = y-1
			if l_y < 0:
				l_y = y
			r_y = y+1
			if r_y >= self.GridSize:
				r_y = y

			for i in range(u_x, d_x+1):
				for j in range(l_y,r_y+1):
					if self.true_Model[i][j] != 2:
						return False
			return True

	## initilization of the class

	def __init__(self):
		# randomly initilize the position of the ships
		# ran_pos_x, ran_pos_y means the position of the first cell of the ship, and dir is the direction,
		# in which 0 means horizontical and 1 means vertical
		for i in range(5):
			flag = 0
			while flag==0:
				ran_pos_x = int(floor(uniform(0,10)))
				ran_pos_y = int(floor(uniform(0,10)))
				ran_dir = int(floor(uniform(0,2)))

				if ran_dir == 0:
					if ran_pos_y+i < self.GridSize:
						non_Conflict = self.CheckConflict(ran_pos_x,ran_pos_y,ran_dir,i)
						if non_Conflict:
							#print "random numbers", i, [ran_pos_x,ran_pos_y,ran_dir]
							for j in range(ran_pos_y,ran_pos_y+i+1):
								self.true_Model[ran_pos_x][j]=1
							flag=1
				else:
					#print "vetical"
					if ran_pos_x+i < self.GridSize:
						non_Conflict = self.CheckConflict(ran_pos_x,ran_pos_y,ran_dir,i)
						if non_Conflict:
							#print "length,random numbers", i, [ran_pos_x,ran_pos_y,ran_dir]
							for i in range(ran_pos_x,ran_pos_x+i+1):
								self.true_Model[i][ran_pos_y]=1
							flag=1 

		# for i in self.true_Model:
		# 	for j in i:
		# 		if j == 2:
		# 			print "0",
		# 		else:
		# 			print "1",
		# 	print " "




	## here the obs is defined as a 1*2 dimension vector
	## the first element is the position, and the 2nd element is the val
	def BeliefUpdate(self, bel0, sample_Mdps, new_obs):
		new_bel = bel0[:]
		count = self.Sample_Size
		# when we receive observation 0
		if new_obs[1] == 0:       
			for i in range(self.Sample_Size):
				if sample_Mdps[i][new_obs[0]] != new_obs[1] or new_bel[i] == 0:
					new_bel[i] = 0
					count -= 1


		#when we receive observation 1
		else:
			lu_corner = new_obs[0] - self.GridSize -1
			ru_corner = new_obs[0] - self.GridSize +1
			ld_corner = new_obs[0] + self.GridSize -1
			rd_corner = new_obs[0] + self.GridSize +1
			for i in range(self.Sample_Size):
				if sample_Mdps[i][new_obs[0]] != new_obs[1] or new_bel[i] == 0:
					new_bel[i] = 0
					count -= 1

				elif lu_corner>=0:
					if sample_Mdps[i][lu_corner] != 0:
						new_bel[i]=0
						count -=1
				elif ru_corner>=0:
					if sample_Mdps[i][ru_corner] != 0:
						new_bel[i]=0
						count -=1
				elif ld_corner<self.GridSize*self.GridSize:
					if sample_Mdps[i][ld_corner] != 0:
						new_bel[i]=0
						count -=1
				elif rd_corner<self.GridSize*self.GridSize:
					if sample_Mdps[i][rd_corner] != 0:
						new_bel[i]=0
						count -=1


		#print count
		for i in range(self.Sample_Size):
			if new_bel[i] != 0:
				new_bel[i] = 1.0/count


		return new_bel 


	# This function calculate the Mean MDP model
	def calMeanMdp(self, belief, sample_Mdps):
		meanMdp = []
		for len in range(self.GridSize*self.GridSize):
			tempAve = 0.0
			for i in range(self.Sample_Size):
				tempAve += belief[i] * sample_Mdps[i][len]
			meanMdp.append(tempAve)
		return meanMdp



	def calRB(self, sample_Mdps, observation, plan_steps):
	 	self.RB = [[0.0 for x in xrange(10)] for x in xrange(10)]

	 	# when we calculate the RB, the expected Reward doesnot change, so we only cal the expected change to the transition functions

	 	cur_Mean_Mdp = self.calMeanMdp(self.bel, sample_Mdps)

	 	for i in range(self.GridSize):
			for j in range(self.GridSize):
	 			if observation[i][j] == 2:  ## Means this action is available
	 				# the case we receive observation 0
	 				prob0 = 1-cur_Mean_Mdp[self.GridSize*i+j]
	 				new_obs0=[i*self.GridSize+j, 0]
	 				temp_bel0 = self.BeliefUpdate(self.bel, sample_Mdps, new_obs0)
	 				temp_Mean_Mdp = self.calMeanMdp(temp_bel0, sample_Mdps)

	 				temp_changT=0.0
	 				for k in range(self.GridSize*self.GridSize):
	 					temp_changT += 2*abs(temp_Mean_Mdp[k]-cur_Mean_Mdp[k])

	 				temp_RB0 = temp_changT*prob0

	 				# the case we receive observation 0
	 				prob1 = cur_Mean_Mdp[self.GridSize*i+j]
	 				new_obs1=[i*self.GridSize+j, 1]
	 				temp_bel1 = self.BeliefUpdate(self.bel, sample_Mdps, new_obs1)
	 				temp_Mean_Mdp1 = self.calMeanMdp(temp_bel1, sample_Mdps)

	 				temp_changT1=0.0
	 				for k in range(self.GridSize*self.GridSize):
	 					temp_changT1 += 2*abs(temp_Mean_Mdp1[k]-cur_Mean_Mdp[k])

	 				temp_RB1 = temp_changT1*prob1

	 				self.RB[i][j] = (2*self.R_max-self.R_min)*plan_steps*plan_steps*plan_steps*(temp_RB0+temp_RB1)


	def ActionSelection(self, sample_Mdps):
		cur_Mean_Mdp = self.calMeanMdp(self.bel, sample_Mdps)
		max_reward=0.0
		max_index=[0,0]
		for i in range (self.GridSize):
			for j in range(self.GridSize):
				if self.obs[i][j] == 2:  ## Means this action is available
					reward_ij=10*cur_Mean_Mdp[i*self.GridSize+j]-1 + self.dis_RB*self.RB[i][j]
					if reward_ij>max_reward:
						max_reward=reward_ij
						max_index=[i,j]
		return max_index

	def CheckFinish(self):
		for i in range(self.GridSize):
			for j in range(self.GridSize):
				if self.true_Model[i][j] == 1:
					if self.obs[i][j] != 1:
						return False

		return True

	def Execution(self, sample_Mdps, action):
		print action

		self.taken_steps += 1

		self.H -= 1

		obser1=1

		if self.true_Model[action[0]][action[1]] == 2:
			obser1=0

		obser=[action[0]*self.GridSize+action[1], obser1]

		if self.true_Model[action[0]][action[1]]==1:

			# Because the ships can not be diagonally adjacent
			ux=action[0]-1
			ly=action[1]-1
			ry=action[1]+1
			if ux>=0 and ly>=0:
				self.obs[ux][ly]=0
			if ux>=0 and ry<self.GridSize:
				self.obs[ux][ry]=0

			dx=action[0]+1
			if dx<self.GridSize and ly>=0:
				self.obs[dx][ly]=0
			if dx<self.GridSize and ry<self.GridSize:
				self.obs[dx][ry]=0
			# Because the ships can not be diagonally adjacent

			self.obs[action[0]][action[1]] = 1
		else:
			self.obs[action[0]][action[1]] = 0
		#self.obs[action[0]][action[1]]=self.true_Model[action[0]][action[1]]

		print "observation:", self.obs
		print "obser:", obser

		## This part test whether we have found all those ships
		isFinished = self.CheckFinish()

		if isFinished:
			return [True,0]

		else:
			self.bel = self.BeliefUpdate(self.bel,sample_Mdps,obser)

			print self.bel

			temp = 0.0
			for i in range(self.Sample_Size):
				temp += self.bel[i]

			if temp > 0.01:
				return [False, 0]
			else:
				return [False, 1]


