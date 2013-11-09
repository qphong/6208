
from math import *
from random import *


d0 = 5
GridSize = [7,7] # numRow, numColumn
NumRock = 8


class MDP:

	rocks = [] # rock locations
	states = [] # states of MDP
	actions = []
	adj = {} # adjacency list
	bel = [] # belief

	H=60  #planning horizon
	R_max=10
	cur_state='s30'

	observation=['g','b']


	def sensorAcc(self, d):
		return 0.5 + 0.5 * 2.0 ** (-d / d0)


	def getCoord(self, state):
		# input state in string
		# return coordinate: row index, column index

		return (int(state[1]), int(state[2]))


	def move(self, coord, act):

		if act == 'n' and coord[0] > 0:
			return (coord[0] - 1, coord[1])
		elif act == 's' and coord[0] < GridSize[0] - 1:
			return (coord[0] + 1, coord[1])
		elif act == 'e':
			if coord[1] < GridSize[1] - 1:
				return (coord[0], coord[1] + 1)
			else:
				return (0,7)
		elif act == 'w' and coord[1] > 0:
			return (coord[0], coord[1] - 1)
		return coord


	def __init__(self):

		self.rocks = [(0,1), (1,5), (2,2), (2,3), (3,6), (5,0), (5,3), (6,2)]
		self.true_rocks=['g','b','g','b','b','g','g','b']

		self.states = [] 
		for i in range(0,GridSize[0]): # row index
			for j in range(0,GridSize[1]): # column index

				self.states.append('s' + str(i) + str(j))
				
				for k in range(0,NumRock):
					self.states.append('s' + str(i) + str(j) + ',o' + str(k) + 'g')
					self.states.append('s' + str(i) + str(j) + ',o' + str(k) + 'b')
		self.states.append('s07')


		self.actions = ['e', 's', 'n', 'w', 'sample']
		for i in range(0,NumRock):
			self.actions.append('check' + str(i))


		for s in self.states[:-1]:
			
			self.adj[s] = {}

			curCoord = self.getCoord(s)

			for a in self.actions[:4]:
				coord = self.move( curCoord, a)
				self.adj[s][a] = [ 's' + str(coord[0]) + str(coord[1]) ]

			if curCoord in self.rocks:
				self.adj[s]['sample'] =  [ s.split(',')[0] ]

			for a in self.actions[5:]:

				self.adj[s][a] = [ s.split(',')[0] + ',o' + a[-1] + 'g']
				self.adj[s][a].append( s.split(',')[0] + ',o' + a[-1] + 'b' )				

		self.adj['s07'] = {}

		self.bel = [0.5] * NumRock


	def calTrans(self):

		self.trans = {}

		for s in self.states:
			
			self.trans[s] = {}
			curCoord = self.getCoord(s)

			for a in self.adj[s].keys(): # possible actions in s
				
				self.trans[s][a] = {}
				for nextS in self.adj[s][a]:

					if a in ['n', 's', 'e', 'w', 'sample']:
						self.trans[s][a][nextS] = 1.0
					else:
						
						rockId = int(a[-1])
						d = sqrt( (curCoord[0] - self.rocks[rockId][0]) * (curCoord[0] - self.rocks[rockId][0])\
							+ (curCoord[1] - self.rocks[rockId][1]) * (curCoord[1] - self.rocks[rockId][1]) )
						accuracy = self.sensorAcc(d)

						if nextS[-1] == 'g':
							self.trans[s][a][nextS] = accuracy * self.bel[rockId] \
								+ (1 - accuracy) * (1 - self.bel[rockId])
						else:
							self.trans[s][a][nextS] = accuracy * (1 - self.bel[rockId]) \
								+ (1 - accuracy) * self.bel[rockId]


	def calRewards(self):

		self.rewards = {}

		for s in self.states:

			self.rewards[s] = {}
			curCoord = self.getCoord(s)

			for a in self.adj[s].keys(): # possible actions in s

				if a == 'e' and curCoord[1] == 6:
					self.rewards[s][a] = 10

				elif a == 'sample':
					
					rockId = 0
					
					for i in range(0, len(self.rocks)):
						if curCoord == self.rocks[i]:
							rockId = i
							break
					
					if rockId == len(self.rocks):
						break
					
					self.rewards[s][a] = 10 * self.bel[rockId] - 10 * (1 - self.bel[rockId])

				else:
					self.rewards[s][a] = 0.0


	def belUpdate(self,curBel,accuracy,obs):
		nextBel=[]
		if obs==self.observation[0]:
			temp1=accuracy*curBel
			temp2=(1-accuracy)*(1-curBel)
		else:
			temp1=(1-accuracy)*curBel
			temp2=accuracy*(1-curBel)

		if temp1 + temp2 == 0:
			nextBel = curBel
		else:
			nextBel=temp1/(temp1+temp2)

		return nextBel

	def calRB(self):
		self.RB={}

		for s in self.states:
			self.RB[s]={}

			curCoord = self.getCoord(s)

			for a in self.adj[s].keys():
				if a[:-1] == 'check':
					rockId = int(a[-1])
					d = sqrt( (curCoord[0] - self.rocks[rockId][0]) * (curCoord[0] - self.rocks[rockId][0])\
							+ (curCoord[1] - self.rocks[rockId][1]) * (curCoord[1] - self.rocks[rockId][1]) )
					accuracy = self.sensorAcc(d)

					rb = 0.0

					for sNext in self.adj[s][a]:

						updatedBel = self.belUpdate(self.bel[rockId], accuracy, sNext[-1])
						updatedRw = updatedBel * 10 - (1 - updatedBel) * 10
						curRw=self.bel[rockId]*10-(1-self.bel[rockId])*10
						rb += self.H*self.trans[s][a][sNext]*(updatedRw-curRw)

						rockCoord = self.rocks[rockId]
						tmpS = 's'+str(rockCoord[0]) + str(rockCoord[1])
						rockObsr = 'o'+str(rockId)
						temp_RB_T=abs(updatedBel-self.trans[tmpS][a][tmpS+ ',' + rockObsr + 'g'])+\
							abs(1 - updatedBel - self.trans[tmpS][a][tmpS + ',' + rockObsr + 'b'])

						rb += self.R_max*self.H**2*self.trans[s][a][sNext]*temp_RB_T

					self.RB[s][a]=rb

				else:
					self.RB[s][a]=0.0


	def execution(self,policy):
		action=policy[self.cur_state]
		print action
		ranNum=random()

		self.H=self.H-1

		nextS = self.cur_state
		curCoord = self.getCoord(self.cur_state)

		if len(self.adj[self.cur_state][action]) > 0:
		
			nextS = self.adj[self.cur_state][action][0]

			if action[:-1] == 'check':

				rockId=int(action[-1])
				d = sqrt( (curCoord[0] - self.rocks[rockId][0]) * (curCoord[0] - self.rocks[rockId][0])\
								+ (curCoord[1] - self.rocks[rockId][1]) * (curCoord[1] - self.rocks[rockId][1]) )
				accuracy = self.sensorAcc(d)

				obsr = nextS.split(',')[1][-1]
				trueV = self.true_rocks[rockId]

				if obsr == trueV:
					probObsr = accuracy
				else:
					probObsr = 1 - accuracy

				if ranNum > probObsr:
					nextS = self.adj[self.cur_state][action][1]

				self.bel[rockId]=self.belUpdate(self.bel[rockId],accuracy,nextS[-1])

				self.cur_state=nextS
				return 1

			elif action == 'sample':
				
				rockId=0
				
				for i in range(len(self.rocks)):
					if curCoord == self.rocks[i]:
						rockId=i
						break
				self.bel[rockId]=0

				self.cur_state=nextS
				return 1
			else: # move
				self.cur_state = nextS
				print 'curstate:', self.cur_state
				return 0

		return 0

		#self.cur_state=nextS


		# if action[:-1]=='check':
			
		# 	rockId=int(action[-1])
		# 	d = sqrt( (curCoord[0] - self.rocks[rockId][0]) * (curCoord[0] - self.rocks[rockId][0])\
		# 					+ (curCoord[1] - self.rocks[rockId][1]) * (curCoord[1] - self.rocks[rockId][1]) )
		# 	accuracy = self.sensorAcc(d)
		# 	self.bel[rockId]=self.belUpdate(self.bel[rockId],accuracy,nextS[-1])

		# 	self.cur_state=nextS
		# 	return 1
		# elif action=='sample':
		# 	rockId=0
		# 	for i in range(len(self.rocks)):
		# 		if curCoord == self.rocks[i]:
		# 			rockId=i
		# 			break
		# 	self.bel[rockId]=0

		# 	self.cur_state=nextS
		# 	return 1
		# else:
		# 	self.cur_state=nextS
		# 	return 0








