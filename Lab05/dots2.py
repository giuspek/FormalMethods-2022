from pysmt.shortcuts import *

problem = [ [1,2,0,0,0], 
			[0,0,0,3,0], 
			[0,3,2,0,0],
			[0,4,0,0,0], 
			[0,0,0,1,4]]

grid = []
for i in range(5):
	l = []
	for j in range(5):
		l.append(Symbol("x{}{}".format(i,j), INT))
	grid.append(l)

solver = Solver()

# Hidden condition: each cell can assume at most of the 4 proposed colors
# Hidden condition: extremes should have one neighbor cell with the same color
# Hidden condition: internal cells should have two neighbor cells with the same color
for i in range(5):
	for j in range(5):
		up = i != 0
		down = i != 4
		left = j != 0
		right = j != 4
		l = []
		if up:
			l.append(Equals(grid[i][j], grid[i-1][j]))
		if down:
			l.append(Equals(grid[i][j], grid[i+1][j]))
		if left:
			l.append(Equals(grid[i][j], grid[i][j-1]))
		if right:
			l.append(Equals(grid[i][j], grid[i][j+1]))
		if problem[i][j] == 0:
			solver.add_assertion(And(GE(grid[i][j], Int(1)), LE(grid[i][j], Int(4))))
			l2 = [Ite(x, Int(1), Int(0)) for x in l]
			solver.add_assertion(GE(Plus(l2), Int(2)))
		else:
			solver.add_assertion(Equals(grid[i][j], Int(problem[i][j])))
			solver.add_assertion(Or(l))

# Easier way to get all assertions as a list (to store into smtlib file)
#print(solver.assertions)

res = solver.solve()
if res:
	solution = list()
	sat_model = {el[0].symbol_name():el[1] for el in solver.get_model()}
	for i in range(5):
		row = ""
		for j in range(5):
			row += str(sat_model["x{}{}".format(i,j)])
		solution.append(row)
	for line in solution:
		print(line)
else:
	print("UNSAT")

