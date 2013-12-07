
from random import *

# SHIP = 1,2,3,4,5,...
NOSHIP = -1
UNKNOWN = 0
FLAG = -2
# type = 1,2,3,4,5

# orientation
HOR = 0
VER = 1

field = []

nShip = 5 # number of ships
nType = 5 # number of types
nRow = 10
nCol = 10

shipCells = []

for r in range(nRow):
	field.append([])
	for c in range(nCol):
		field[r].append(UNKNOWN)


def createField(inShipCells, noShipCells):

	global field
	global shipCells

	shipCells = inShipCells[:]

	c = 1
	for (x,y) in shipCells:
		field[x][y] = c
		c = c + 1

	for (x,y) in noShipCells:
		field[x][y] = NOSHIP


def isShipAt(x,y):

	return field[x][y] > 0 or field[x][y] == FLAG


def isValid(field, type, top, left, orient):

	if orient == HOR:
		
		for i in range(left,left + type):
			if field[top][i] == NOSHIP or field[top][i] == FLAG:
				return False

		if top > 0:
			for i in range(left,left + type):
				if isShipAt(top - 1,i):
					return False

		if top + 1 < nRow:
			for i in range(left,left + type):
				if isShipAt(top + 1,i):
					return False

		if left > 0:
			if isShipAt(top,left - 1) or \
				(top > 0 and isShipAt(top - 1,left - 1)) or \
				(top + 1 < nRow and isShipAt(top + 1, left - 1)):
				return False

		if left + type < nCol:
			if isShipAt(top,left + type) or \
				(top > 0 and isShipAt(top - 1, left + type)) or \
				(top + 1 < nRow and isShipAt(top + 1, left + type)):
				return False


	if orient == VER:

		for i in range(top,top + type):
			if field[i][left] == NOSHIP:
				return False

		if left > 0:
			for i in range(top,top + type):
				if isShipAt(i,left - 1):
					return False

		if left + 1 < nCol:
			for i in range(top,top + type):
				if isShipAt(i,left + 1):
					return False

		if top > 0:
			if isShipAt(top - 1,left) or \
				(left > 0 and isShipAt(top - 1, left - 1)) or \
				(left + 1 < nCol and isShipAt(top - 1, left + 1)):
				return False

		if top + type < nRow:
			if isShipAt(top + type, left) or \
				(left > 0 and isShipAt(top + type, left - 1)) or \
				(left + 1 < nCol and isShipAt(top + type, left + 1)):
				return False

	return True


def getPossibleConstraintedLayout():

	# ship: (type,top,left,orientation)
	results = getPossibleConstraintedLayoutR(0, 0, 0, [])
	return results


def tryVertical(t, mask, maskT, idx, sols):
	global shipCells
	global field

	# vertical:top
	startTop = shipCells[idx][0] - t + 1
	if startTop < 0:
		startTop = 0

	endTop = shipCells[idx][0] + t - 1
	if endTop >= nRow:
		endTop = nRow - t
	else:
		endTop = shipCells[idx][0]

	tmp = [0] * t # for saving field
					
	results = []

	shuffleTop = range(startTop,endTop + 1)
	shuffle(shuffleTop)
	for i in shuffleTop:
		if isValid(field, t, i, shipCells[idx][1], VER):
			# flag ship
			tmpMask = mask
			tmpMaskT = maskT
			for j in range(i,i + t):
				tmp[j - i] = field[j][shipCells[idx][1]]
				if field[j][shipCells[idx][1]] <= 0:
					field[j][shipCells[idx][1]] = FLAG
				else:
					tmpMask = tmpMask | (1 << (field[j][shipCells[idx][1]] - 1))

			tmpMask = tmpMask | (1 << idx)
			tmpMaskT = tmpMaskT | (1 << (t - 1))

			sols.append([t, i, shipCells[idx][1], VER])
			tmpR = getPossibleConstraintedLayoutR(tmpMask, tmpMaskT, idx + 1, \
				sols)
			results.extend(tmpR)
			sols.pop()

			for j in range(i,i + t):
				field[j][shipCells[idx][1]] = tmp[j - i]

	return results


def tryHorizontal(t, mask, maskT, idx, sols):
	global shipCells
	global field

	# horizontal:left
	startLeft = shipCells[idx][1] - t + 1
	if startLeft < 0:
		startLeft = 0

	endLeft = shipCells[idx][1] + t - 1
	if endLeft >= nCol:
		endLeft = nCol - t
	else:
		endLeft = shipCells[idx][1]

	results = []
	shuffleLeft = range(startLeft, endLeft + 1)
	shuffle(shuffleLeft)
	for i in shuffleLeft:
		if isValid(field, t, shipCells[idx][0], i, HOR):
			#flag ship
			tmp = field[shipCells[idx][0]][i:i+t]
			tmpMask = mask
			tmpMaskT = maskT
			for j in range(i,i+t):
				tmp[j-i] = field[shipCells[idx][0]][j]
				if field[shipCells[idx][0]][j] <= 0:
					field[shipCells[idx][0]][j] = FLAG
				else:
					tmpMask = tmpMask | (1 << (field[shipCells[idx][0]][j] - 1))

			tmpMask = tmpMask | (1 << idx)
			tmpMaskT = tmpMaskT | (1 << (t - 1))

			sols.append([t, shipCells[idx][0], i, HOR])
			tmpR = getPossibleConstraintedLayoutR(tmpMask, tmpMaskT, idx + 1, \
				sols)
			results.extend(tmpR)
			sols.pop()

			field[shipCells[idx][0]][i:i+t] = tmp[:]

			for j in range(i,i + t):
				field[shipCells[idx][0]][j] = tmp[j - i]

	return results


def getPossibleConstraintedLayoutR(mask, maskT, idx, sols):

	global field
	global shipCells

	if idx == len(shipCells):
		r = [sols[:]]
		return r

	results = []

	if mask & (1 << idx) != 0:
		tmpR = getPossibleConstraintedLayoutR(mask, maskT, idx + 1, sols)
		results.extend(tmpR)
	else:
		shuffleType = range(1,6)
		shuffle(shuffleType)
		for t in shuffleType:
			if maskT & (1 << (t - 1)) == 0: # available types

				if t == 1: # only 1 orientation
					tmpR = tryHorizontal(1, mask, maskT, idx, sols)
					results.extend(tmpR)
				else:
					if random() >= 0.5:
						tmpR = tryHorizontal(t, mask, maskT, idx, sols)
						results.extend(tmpR)
						tmpR = tryVertical(t, mask, maskT, idx, sols)
						results.extend(tmpR)
					else:
						tmpR = tryVertical(t, mask, maskT, idx, sols)
						results.extend(tmpR)
						tmpR = tryVertical(t, mask, maskT, idx, sols)
						results.extend(tmpR)

	return results


sizeLimit = 0 # limit size for buildFullLayoutR recursion


def getFullLayout(constraintedLayouts, numberOfLayout):

	numLayoutPerConstraintLayout = numberOfLayout / len(constraintedLayouts) + 1
	results = []
	for l in constraintedLayouts:
		tmpR = buildFullLayout(l, numLayoutPerConstraintLayout)
		results.extend(tmpR)
	return results


def buildFullLayout(curLayout, limitSz):
	# limitS: maximum number of layout needed

	global sizeLimit

	tmpField = []
	for r in range(nRow):
		tmpField.append([UNKNOWN] * nCol)

	possibleType = [1,2,3,4,5]
	for l in curLayout:
		type = l[0]
		top = l[1]
		left = l[2]
		orient = l[3]

		possibleType.remove(type)

		if orient == VER:
			for i in range(top, top + type):
				tmpField[i][left] = 1
		else: # orient == HOR
			for i in range(left, left + type):
				tmpField[top][i] = 1

	possibleShipLoc = []
	for r in range(nRow):
		for i in range(nCol):
			if isValid(tmpField, 1, r, i, VER):
				possibleShipLoc.append([r,i])

	shuffle(possibleShipLoc)
	shuffle(possibleType)

	sizeLimit = limitSz
	return buildFullLayoutR(tmpField, possibleShipLoc, possibleType, curLayout)


def buildFullLayoutR(tmpField, possibleShipLoc, possibleType, sols):

	global sizeLimit

	if len(possibleType) == 0:
		sizeLimit -= 1
		return [sols[:]]

	results = []
	for i in range(len(possibleShipLoc)):
		for j in range(len(possibleType)):
			loc = possibleShipLoc[i]
			t = possibleType[j]

			if t == 1:
				if loc[0] + t < nRow and isValid(tmpField, t, loc[0], loc[1], VER):
					tmpField[loc[0]][loc[1]] = 1
					sols.append([t, loc[0], loc[1], VER])
					tmpR = buildFullLayoutR(tmpField, possibleShipLoc[i + 1:], \
						possibleType[:j] + possibleType[j + 1:], sols)
					results.extend(tmpR)
					sols.pop()
					tmpField[loc[0]][loc[1]] = UNKNOWN
					if sizeLimit == 0:
						return results
			else:

				if random() > 0:

					if loc[0] + t < nRow and isValid(tmpField, t, loc[0], loc[1], VER):
						for r in range(loc[0], loc[0] + t):
							tmpField[r][loc[1]] = 1
						sols.append([t, loc[0], loc[1], VER])
						tmpR = buildFullLayoutR(tmpField, possibleShipLoc[i + 1:], \
							possibleType[:j] + possibleType[j + 1:], sols)
						results.extend(tmpR)
						sols.pop()
						for r in range(loc[0], loc[0] + t):
							tmpField[r][loc[1]] = UNKNOWN
						if sizeLimit == 0:
							return results

					if loc[1] + t < nCol and isValid(tmpField, t, loc[0], loc[1], HOR):
						for c in range(loc[1], loc[1] + t):
							tmpField[loc[0]][c] = 1
						sols.append([t, loc[0], loc[1], HOR])
						tmpR = buildFullLayoutR(tmpField, possibleShipLoc[i + 1:], \
							possibleType[:j] + possibleType[j + 1:], sols)
						results.extend(tmpR)
						sols.pop()
						for c in range(loc[1], loc[1] + t):
							tmpField[loc[0]][c] = UNKNOWN
						if sizeLimit == 0:
							return results

				else: # repetition code in reverse order!!!

					if loc[1] + t < nCol and isValid(tmpField, t, loc[0], loc[1], HOR):
						for c in range(loc[1], loc[1] + t):
							tmpField[loc[0]][c] = 1
						tmpR = buildFullLayoutR(tmpField, possibleShipLoc[i + 1:], \
							possibleType[:j] + possibleType[j + 1:], sols)
						results.extend(tmpR)
						for c in range(loc[1], loc[1] + t):
							tmpField[loc[0]][c] = UNKNOWN
						if sizeLimit == 0:
							return results

					if loc[0] + t < nRow and isValid(tmpField, t, loc[0], loc[1], VER):
						for r in range(loc[0], loc[0] + t):
							tmpField[r][loc[1]] = 1
						tmpR = buildFullLayoutR(tmpField, possibleShipLoc[i + 1:], \
							possibleType[:j] + possibleType[j + 1:], sols)
						results.extend(tmpR)
						for r in range(loc[0], loc[0] + t):
							tmpField[r][loc[1]] = UNKNOWN
						if sizeLimit == 0:
							return results

	return results


def visualizeField():

	global field
	for r in field:
		for i in r:
			print i,
		print " "


def test(shipC, noShipC):

	createField(shipC, noShipC)
	constraintedLayouts = getPossibleConstraintedLayout()
	# print "Constrainted results:"
	# for r in constraintedLayouts:
	# 	print r
	# print " "

	results = getFullLayout(constraintedLayouts, 200)
	print "Results:"
	for r in results:
		print r
	print len(results)





