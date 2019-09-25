## Sudoku - Generator/Solver
## Main collaborators:
## Adrián Carretero
## Jonathan Sanchez
## Using python 3 

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


def main():
	init_dicts()
	print(square_iden)
	print(position_iden)

if __name__ == "__main__":
	main()
