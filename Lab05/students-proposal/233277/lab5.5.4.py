from copy import deepcopy
from symtable import Symbol
from pysmt.shortcuts import *

# 1 = red, 2 = yellow, 3 = blue, 4 = green
puzzle_map = [
    [1, 2, 0, 0, 0],
    [0, 0, 0, 3, 0],
    [0, 3, 2, 0, 0],
    [0, 4, 0, 0, 0],
    [0, 0, 0, 1, 4]
]

vars = {"x{}{}".format(i, j): Symbol("x{}{}".format(i, j), INT) for i in range(5) for j in range(5)}

s = Solver()

# Each cell take 1 value in range(1,4), fill in constrained cells
for i in range(5):
    for j in range(5):
        if puzzle_map[i][j] != 0:
            s.add_assertion(Equals(vars["x{}{}".format(i, j)], Int(puzzle_map[i][j])))
        else:
            s.add_assertion(And(GE(vars["x{}{}".format(i, j)], Int(1)), LE(vars["x{}{}".format(i, j)], Int(4))))

# Add constraints
for i in range(5):
    for j in range(5):
        constraint = []
        if i != 0:
            constraint.append(Equals(vars["x{}{}".format(i, j)], vars["x{}{}".format(i - 1, j)]))
        if j != 0:
            constraint.append(Equals(vars["x{}{}".format(i, j)], vars["x{}{}".format(i, j - 1)]))
        if i != 4:
            constraint.append(Equals(vars["x{}{}".format(i, j)], vars["x{}{}".format(i + 1, j)]))
        if j != 4:
            constraint.append(Equals(vars["x{}{}".format(i, j)], vars["x{}{}".format(i, j + 1)]))
        if puzzle_map[i][j] == 0:
            real_constraint = []
            for k in range(len(constraint) - 1):
                for h in range(k + 1, len(constraint)):
                    real_constraint.append([constraint[k], constraint[h]])
            s.add_assertion(Or(And(cons) for cons in real_constraint))
        else:
            s.add_assertion(Or(constraint))


if s.solve():
    print("SAT")
    answer = deepcopy(puzzle_map)
    for var in vars:
        answer[int(var[1])][int(var[2])] = int(str(s.get_value(vars[var])))
    for r in answer:
        for e in r:
            print(e, end="  ")
        print("")
else:
    print("UNSAT")