from pysmt.shortcuts import *

vars = {"x{}{}".format(i, j): Symbol("x{}{}".format(i, j), BOOL) for i in range(4) for j in range(4)}

s = Solver()

# All 4 pin must be connected, each pin connected once
for i in range(4):
    s.add_assertion(ExactlyOne(vars["x{}{}".format(i, j)] for j in range(4)))

# No 2 pin at the same time
for j in range(4):
    s.add_assertion(ExactlyOne(vars["x{}{}".format(i, j)] for i in range(4)))

# No diagonal
for j in range(3):
    s.add_assertion(Not(And(vars["x0{}".format(j)], vars["x3{}".format(j + 1)])))
    s.add_assertion(Not(And(vars["x1{}".format(j)], vars["x2{}".format(j + 1)])))
    s.add_assertion(Not(And(vars["x0{}".format(j + 1)], vars["x3{}".format(j)])))
    s.add_assertion(Not(And(vars["x1{}".format(j + 1)], vars["x2{}".format(j)])))

# Calculate number of combination
num_combin = 0
while s.solve():
    print("Solution {}:".format(num_combin + 1))
    num_combin += 1
    s.push()
    old_sol = []
    grid_map = [[0, 0], [0, 0]]
    for var in vars:
        if str(s.get_value(vars[var])) == 'True':
            old_sol.append(vars[var])
            grid_map[int(var[1]) // 2][int(var[1]) % 2] = int(var[2]) + 1
    for r in grid_map:
        for e in r:
            print(e, end="  ")
        print("")
    old_sol = And(old_sol)
    s.add_assertion(Not(old_sol))
print("Number of combinations: {}".format(num_combin))