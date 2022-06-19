from copy import deepcopy
from pysmt.shortcuts import *

kakuro_map = [
    [-1, -1, -1, -1, -1],
    [-1, 0, 0, 0, -1],
    [-1, 0, 0, 0, -1],
    [-1, 0, 0, -1, -1],
    [-1, -1, 0, 0, 0],
    [-1, -1, 0, 0, 0]
]

vars = {"x{}{}".format(i, j): Symbol("x{}{}".format(i, j), INT) for i in range(6) for j in range(5)}

s = Solver()

# Adding cells in grid, each blank cell can be filled with a number between 1 and 9
for i in range(6):
    for j in range(5):
        if kakuro_map[i][j] == -1:
            s.add_assertion(Equals(vars["x{}{}".format(i, j)], Int(-1)))
        else:
            s.add_assertion(And(GE(vars["x{}{}".format(i, j)], Int(1)), LE(vars["x{}{}".format(i, j)], Int(9))))

# Adding constraint: sum of rows and columns & they must be different
s.add_assertion(And(Equals(Int(9), Plus(vars["x1{}".format(j)] for j in range(1, 4))), AllDifferent(vars["x1{}".format(j)] for j in range(1, 4))))
s.add_assertion(And(Equals(Int(13), Plus(vars["x2{}".format(j)] for j in range(1, 4))), AllDifferent(vars["x2{}".format(j)] for j in range(1, 4))))
s.add_assertion(And(Equals(Int(13), Plus(vars["x3{}".format(j)] for j in range(1, 3))), AllDifferent(vars["x3{}".format(j)] for j in range(1, 3))))
s.add_assertion(And(Equals(Int(7), Plus(vars["x4{}".format(j)] for j in range(2, 5))), AllDifferent(vars["x3{}".format(j)] for j in range(2, 5)))) # If this condition is commented out
s.add_assertion(And(Equals(Int(19), Plus(vars["x4{}".format(j)] for j in range(2, 5))), AllDifferent(vars["x3{}".format(j)] for j in range(2, 5)))) # and this one, it will be SAT

s.add_assertion(And(Equals(Int(9), Plus(vars["x{}1".format(i)] for i in range(1, 4))), AllDifferent(vars["x{}1".format(i)] for i in range(1, 4))))
s.add_assertion(And(Equals(Int(34), Plus(vars["x{}2".format(i)] for i in range(1, 6))), AllDifferent(vars["x{}2".format(i)] for i in range(1, 6))))
s.add_assertion(And(Equals(Int(4), Plus(vars["x{}3".format(i)] for i in range(1, 3))), AllDifferent(vars["x{}3".format(i)] for i in range(1, 3))))
s.add_assertion(And(Equals(Int(11), Plus(vars["x{}3".format(i)] for i in range(4, 6))), AllDifferent(vars["x{}3".format(i)] for i in range(4, 6))))
s.add_assertion(And(Equals(Int(3), Plus(vars["x{}4".format(i)] for i in range(4, 6))), AllDifferent(vars["x{}4".format(i)] for i in range(4, 6))))

if s.solve():
    print("SAT")
    answer = deepcopy(kakuro_map)
    for var in vars:
        answer[int(var[1])][int(var[2])] = int(str(s.get_value(vars[var])))
        if int(str(s.get_value(vars[var]))) == -1:
            answer[int(var[1])][int(var[2])] = "X"
    for r in answer:
        for e in r:
            print(e, end = "  ")
        print("")
else:
    print("UNSAT")