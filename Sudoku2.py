import random as rand
import time


sudoku=[]
fulldict={}

##Fulldict explanation positions: 0 - Possible values
## 1 - Square, 2 - Positions same row, 3 - Position same column

def init_sudoku():
	for x in range(9):
		sudoku.append([])
		for y in range(9):
			sudoku[x].append(0)

def samerow(pos):
	return [(pos[0], yy) for yy in range(9) if yy!=pos[1]]

def samecolumn(pos):
	return [(xx, pos[1]) for xx in range(9) if xx != pos[0]]

def init_dict():
	possibilities=[1,2,3,4,5,6,7,8,9]
	for x in range(9):
		for y in range(9):
			fulldict[(x, y)]=[possibilities.copy()]
			z=0
			if x in [0,1,2]: z+=0
			if x in [3,4,5]: z+=3
			if x in [6,7,8]: z+=6

			if y in [0,1,2]: z+=0
			if y in [3,4,5]: z+=1
			if y in [6,7,8]: z+=2
			fulldict[(x, y)].append(z)

			fulldict[(x, y)].append(samerow((x,y)))

			fulldict[(x, y)].append(samecolumn((x,y)))

def clearall():
	sudoku.clear()
	fulldict.clear()


def findlower():
	minvalue=min([len(fulldict[(key)][0]) for key in fulldict])
	return [ (keys) for keys in fulldict if len(fulldict[keys][0]) == minvalue]


def minimizepossibilities(value, pos):
	for nrow in fulldict[pos][2]:
		if value in fulldict[nrow][0]: fulldict[nrow][0].remove(value)
		if pos in fulldict[nrow][2]: fulldict[nrow][2].remove(pos)
	
	for ncolumn in fulldict[pos][3]:
		if value in fulldict[ncolumn][0]: fulldict[ncolumn][0].remove(value)
		if pos in fulldict[ncolumn][3]: fulldict[ncolumn][3].remove(pos)

	for keys in fulldict:
		if fulldict[keys][1]==fulldict[pos][1]:
			if value in fulldict[keys][0]: fulldict[keys][0].remove(value)
			if pos in fulldict[keys][2]: fulldict[keys][2].remove(pos)
			if pos in fulldict[keys][3]: fulldict[keys][3].remove(pos)
	del fulldict[pos]


def generate_sud():
	try:
		for i in range(81):
			lowercells=findlower()
			pos=rand.choice(lowercells)
			value=rand.choice(fulldict[pos][0])
			sudoku[pos[0]][pos[1]]=value
			minimizepossibilities(value, pos)
		return True
	except: return False

def checkvalues():
	for x in fulldict:
		values=[]
		for pos in samerow(x):
			if pos in fulldict: 
				for value in fulldict[pos][0]:
					if value not in values: values.append(value)

		for pos in samecolumn(x):
			if pos in fulldict:
				for value in fulldict[pos][0]:
					if value not in values: values.append(value)			
			
		for y in fulldict:
			if fulldict[y][1] == fulldict[x][1]:
				for value in fulldict[y][0]:
					if value not in values: values.append(value)
		fulldict[x][0].clear()
		fulldict[x][0]=values		


def erasevalue(pos):
	value=sudoku[pos[0]][pos[1]]
	sudoku[pos[0]][pos[1]]=0

	z=0
	if pos[0] in [0,1,2]: z+=0
	if pos[0] in [3,4,5]: z+=3
	if pos[0] in [6,7,8]: z+=6

	if pos[1] in [0,1,2]: z+=0
	if pos[1] in [3,4,5]: z+=1
	if pos[1] in [6,7,8]: z+=2
	fulldict[pos]=[[value]]
	fulldict[pos].append(z)
	fulldict[pos].append(samerow(pos))
	fulldict[pos].append(samecolumn(pos))
	checkvalues()





def main():
	init_sudoku()
	init_dict()
	done=generate_sud()
	while(done==False):
		clearall()
		init_sudoku()
		init_dict()
		done=generate_sud()
	for x in sudoku:
		print (x)
	print()
	allpositions=[(x, y) for x in range(9) for y in range(9)]
	for y in range(25):
		erasingpos=rand.choice(allpositions)
		allpositions.remove(erasingpos)
		print(erasingpos)
		erasevalue(erasingpos)
		for x in sudoku:
			print(x)
		print()
	
if __name__ == "__main__":
	main()
