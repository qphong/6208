from random import *

Upper_Limit_Tries = 500

Upper_Limit_Each_Model = 60

def Group_Adjecent_1s(obs, GridSize):
	temp_obs = obs[:]

	group=[]

	distinguished = 0

	for i in range(0,GridSize):
		for j in range(0.GridSize):
			if temp_obs[i][j] == 1:
				if j+1< GridSize:
					if temp_obs[i][j+1] == 1:
						size = 0
						upper=i
						left=j
						dir=0
						for k in range(j,GridSize):
							if temp_obs[i][k] == 1:
								size += 1
								temp_obs[i][k]=0
							else:
								break
						group.append([size,upper,left,dir])
						distinguished += 1

				if i+1<GridSize:
					if temp_obs[i+1][j] == 1:
						size = 0
						upper=i
						left=j
						dir=1
						for k in range(i,GridSize):
							if temp_obs[k][j] == 1:
								size += 1
								temp_obs[k][j]=0
							else:
								break
						group.append([size,upper,left,dir])
						distinguished += 1

	for i in range(0, GridSize):
		for j in range(0, GridSize):
			


def Randomly_Find_Possible_Models(obs, GridSize):
	group_result = Group_Adjecent_1s(obs)

def getRandomSols(obs, GridSize, particle_size):

	list_possible_models = Randomly_Find_Possible_Models(obs, GridSize)

