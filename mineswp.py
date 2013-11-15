
from random import *

class MineSWP:
	
	# use bit operator for REVEALED and HIDDEN
	REVEALED = 1
	HIDDEN = 0

	MINE = -1

	# for surrounding cell operations
	tmp0 = [-1,-1,-1,0,0,1,1,1]
	tmp1 = [-1,0,1,-1,1,-1,0,1]


	def __init__(self, size, numMines):
		# size: [number of rows, number of columns]

		self.size = size[:]
		self.numMines = numMines
		self.numRevealed = 0 # number of cells revealed
		self.status = self.HIDDEN # set (i*size[1] + j)th bit to 1 if revealed
		# all cells are hidden

		# create grid cell of zeros ()
		self.grid = []
		for i in range(self.size[0]):	

			self.grid.append([])
			for j in range(self.size[1]):
				self.grid[i].append(0)

		# random position of mines
		locY = sample(range(self.size[0]), numMines)
		locX = sample(range(self.size[1]), numMines)

		for i in range(numMines):
			self.grid[locY[i]][locX[i]] = 1

		tmp = []
		for i in range(self.size[0]):
			tmp.append([])
			tmp[i] = self.grid[i][:]

		# calculate number of MINE around an empty cell
		for i in range(self.size[0]):
			for j in range(self.size[1]):

				if tmp[i][j] != 1:
					for k in range(8):

						i0 = i + self.tmp0[k]
						j0 = j + self.tmp1[k]

						if i0 >= 0 and i0 < size[0] \
							and j0 >= 0 and j0 < size[1]:

							self.grid[i][j] += tmp[i0][j0] # since MINE = -1

		# assign MINE to cells containing mine
		for i in range(numMines):
			self.grid[locY[i]][locX[i]] = self.MINE


	def setBit(self, pos, val):
		# val in {0,1}
		if val == 1: # REVEALED
			self.status |= (1 << (pos[0] * self.size[1] + pos[1]))
		if val == 0: # HIDDEN
			self.status &= ~(1 << (pos[0] * self.size[1] + pos[1]))


	def getBit(self, pos):

		if self.status & (1 << (pos[0] * self.size[1] + pos[1])) != 0:
			return 1 # REVEALED
		return 0 # HIDDEN


	def reveal(self, pos):
	# return list of all cells revealed and their values
	# [ [ [y,x],val ], ...]

		if self.getBit(pos) == self.REVEALED:
			return []

		self.setBit(pos, self.REVEALED)
		v = self.grid[pos[0]][pos[1]]

		l = []
		if v == 0: # reveal surrounding cells
			for i in range(8):
				i0 = pos[0] + self.tmp0[i]
				j0 = pos[1] + self.tmp1[i]

				if i0 >= 0 and i0 < self.size[0] \
					and j0 >= 0 and j0 < self.size[1]:

					l += self.reveal([i0,j0])

		l.append([pos, v])

		return l


	def visualize(self):
	# display the grid

		for i in range(self.size[0]):

			tmp = ""
			for j in range(self.size[1]):

				if self.getBit([i,j]) == self.REVEALED:
					if self.grid[i][j] == self.MINE:
						tmp += "M"
					else:
						tmp += str(self.grid[i][j])
				else:
					tmp += "*"

			print tmp















