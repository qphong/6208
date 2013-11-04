
from math import *


d0 = 20
GridSize = [7,7] # numRow, numColumn
NumRock = 8


class MDP:

	rocks = [] # rock locations
	states = [] # states of MDP
	actions = []
	adj = {} # adjacency list
	bel = [] # belief


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

		self.rocks = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (1,0)]

		self.states = [] 
		for i in range(0,GridSize[0]): # row index
			for j in range(0,GridSize[1]): # column index

				self.states.append('s' + str(i) + str(j))
				
				for k in range(0,NumRock):
					self.states.append('s' + str(i) + str(j) + ',o' + str(k) + 'g')
					self.states.append('s' + str(i) + str(j) + ',o' + str(k) + 'b')
		self.states.append('s07')


		self.actions = ['n', 's', 'e', 'w', 'sample']
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

