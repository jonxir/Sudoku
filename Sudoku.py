## Sudoku - Generator/Solver
## Main collaborators:
## Adrián Carretero
## Jonathan Sanchez
## Using python 3

import random as rand

sudoku=[]  		  ##Game variable
square_iden = {}  ## We will identify which positions are in each square
position_iden= {} ## We will identify the square of each position

#Print Menu

def print_Menu():
	print(" ----------------- Menu ----------------- ")
	print("1. Solve sudoku")
	print("2. Generate Solved Sudoku")
	print("3. Check Ranking")							#Prints a ranking with the fastest players solving the sudoku (by time)
	#More options are welcome
	print(" ---------------------------------------- ")
	option = input("Select one of the above options: ")
	return option

## Initiation of an empty sudoku
def init_sudoku():
	for x in range(9):
		sudoku.append([])
		for y in range(9):
			sudoku[x].append(0)


#Initiation of both dicts
def init_dicts():
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

#'n' is a value ;; 'pos' is a tuple
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
	else: return False

#Should be finished. CHECK!
def generate_sud():
	for x in range(9):
		for i in range(9):
			value=(rand.randint(1,9))
			while(!(isvalidnum(value, (x,i)))):
				value = (rand.randint(1,9))
			sudoku[x][i]=value

#Prints a grade with a completed sudoku
def print_sud():
	index = 0
	for x in range(9):
		if(x == 0 or x == 3 or x == 6):
			while(index < 9):
				print('==', sep = '', end='\n')
				index += 1
			index = 0
		for i in range(9):
			if(i != 3 or i != 6):
				print('|', end='')
			else:
				print('||', end='')
			print(sudoku[x][i], end='')
		print('||')
		while(index < 9):
			print('--', sep = '', end='\n')
			index += 1
		index = 0

	while(index < 9):
		print('==', sep='', end='\n')
		index+=1

#Prints a rank with username and time from a local file in the same directory
#def get_rank():


def main():
	option = print_Menu()
	init_sudoku()
	init_dicts()

	if(option == 1):
		generate_sud()
		#More functions to be implemented

	if(option == 2):
		generate_sud()
		print_sud()

	if(option == 3):
		get_rank()

if __name__ == "__main__":
	main()
