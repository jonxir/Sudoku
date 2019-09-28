## Sudoku - Generator/Solver
## Main collaborators:
## Adrián Carretero
## Jonathan Sanchez
## Using python 3

import random as rand
import time


sudoku=[]  		  ##Game variable
square_iden = {}  ## We will identify which positions are in each square
position_iden= {} ## We will identify the square of each position
possibilities= {}
columneigh= {}
rowneigh= {}
#Print Menu
def print_Menu():
	print(" ----------------- Menu ----------------- ")
	print("1. Solve sudoku")
	print("2. Generate Solved Sudoku")
	print("3. Check Ranking")							#Prints a ranking with the fastest players solving the sudoku (by time)
	#More options are welcome
	print(" ---------------------------------------- ")
	option = input("Select one of the above options: ")
	return int(option)

## Initiation of an empty sudoku
def init_sudoku():
	for x in range(9):
		sudoku.append([])
		for y in range(9):
			sudoku[x].append(0)


#Initiation of both dicts
def init_dicts():
	possible=[1,2,3,4,5,6,7,8,9]
	for x in range(9):
		for y in range(9):
			z=0
			if x in [0,1,2]: z+=0
			if x in [3,4,5]: z+=3
			if x in [6,7,8]: z+=6

			if y in [0,1,2]: z+=0
			if y in [3,4,5]: z+=1
			if y in [6,7,8]: z+=2
			if z not in square_iden: square_iden[z]=[(x,y)]
			else: square_iden[z].append((x,y))

			position_iden[(x, y)]=z
			possibilities[(x, y)]=possible.copy()

def populateneigh():
	for pos in position_iden:
		for x in range(9):
			for y in range(9):
				if pos != (x,y):
					if x == pos[0]:
						if pos in rowneigh: rowneigh[pos]+=[(x,y)]
						else: rowneigh[pos]=[(x,y)]
					elif y == pos[1]:
						if pos in columneigh: columneigh[pos]+=[(x,y)]
						else: columneigh[pos]=[(x,y)]




def extractmin():
	return (min([len(i) for i in possibilities.values()]))

def extractlower():
	lower = extractmin()
	print(lower)
	return [ x for x in possibilities if (len(possibilities[x]) == lower)]




def minimizepossibilities(n, pos):
	first=True
	for rown in rowneigh[pos]:
		if n in possibilities[rown]: possibilities[rown].remove(n)
		if pos in rowneigh[rown]: rowneigh[rown].remove(pos)

	for column in columneigh[pos]:
		if n in possibilities[column]: possibilities[column].remove(n)
		if pos in columneigh[column]: columneigh[column].remove(pos)

	for tuplepos in square_iden[position_iden[pos]]:
		if n in possibilities[tuplepos]: possibilities[tuplepos].remove(n)

	square_iden[position_iden[pos]].remove(pos)
	del rowneigh[pos]
	del columneigh[pos]
	del possibilities[pos]
	"""
	for rown, column in zip(rowneigh[pos], columneigh[pos]):
		if n in possibilities[rown]: possibilities[rown].remove(n)
		if n in possibilities[column]: possibilities[column].remove(n)

		for tuplepos in square_iden[position_iden[pos]]:
				if n in possibilities[tuplepos]: possibilities[tuplepos].remove(n)
		if pos in rowneigh[rown]: rowneigh[rown].remove(pos)
		if pos in columneigh[column]: columneigh[column].remove(pos)

		if first == True:
			square_iden[position_iden[pos]].remove(pos)
			del rowneigh[pos]
			del columneigh[pos]
			del possibilities[pos]
			first=False
	"""

#Should be finished. CHECK!
def generate_sud():
	try:
		for i in range(81):
			lowercells=extractlower()
			print(lowercells)
			selection=rand.choice(lowercells)
			value=rand.choice(possibilities[selection])
			sudoku[selection[0]][selection[1]]=value
			print_sud()
			minimizepossibilities(value, selection)
		return True
	except:
		return False



#Prints a grade with a completed sudoku
def print_sud():
	for x in range(9):
		if(x == 0 or x == 3 or x == 6): print('=='*14)

		for i in range(9):
			if(i == 3 or i == 6): print(" || ", end='')

			else: print('|', end='')

			print(sudoku[x][i], end='')

		print(" || ")
	print('=='*14)

def clearall():

	sudoku.clear()
	square_iden.clear()
	position_iden.clear()
	possibilities.clear()
	columneigh.clear()
	rowneigh.clear()

#Prints a rank with username and time from a local file in the same directory
#def get_rank():

def main():
	#option = print_Menu()
	init_sudoku()
	init_dicts()
	populateneigh()
	done=generate_sud()
	while(done == False):
		clearall()
		init_sudoku()
		init_dicts()
		populateneigh()
		done=generate_sud()



	'''if(option == 1):
		generate_sud()
		#More functions to be implemented

	if(option == 2):
		generate_sud()
		print_sud()

	if(option == 3):
		get_rank() '''

if __name__ == "__main__":
	main()



#######################################################################

"""

def validsquare(n, pos):
	for tuplepos in square_iden[position_iden[pos]]:
		if n == sudoku[tuplepos[0]][tuplepos[1]]: return False
	return True

#'n' is a value ;; 'pos' is a tuple
def isvalidnum(n, pos):
	for val in sudoku[pos[0]]:
		if val==n: return False
	for column in sudoku:
		if column[pos[1]] == n: return False
	if validsquare(n, pos): return True
	else: return False """
