## Sudoku - Generator/Solver
## Main collaborators:
## Adrián Carretero
## Jonathan Sanchez
## Using python 3 

import random as rand

sudoku=[]  ##Game variable
square_iden = {}  ## We will identify which positions are in each square
position_iden= {} ## We will identify the square of each position

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

def validsquare(n, pos):
	for tuplepos in square_iden[position_iden[pos]]:
		if n == sudoku[tuplepos[0]][tuplepos[1]]: return False
	return True

def isvalidnum(n, pos):
	for val in sudoku[pos[0]]:
		if val==n: return False
	for column in sudoku:
		if column[pos[1]] == n: return False
	if validsquare(n, pos): return True
	else: return False

def generate_sud(): ##Not finished
	for x in range(9):
		for i in range(9):
			value=(rand.randint(1,9))
			if isvalidnum(value, (x, i)):
			  sudoku[x][i]=value

		




def main():
	init_sudoku()
	init_dicts()
	#generate_sud()	
if __name__ == "__main__":
	main()
