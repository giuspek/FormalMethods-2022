from copy import deepcopy
from pysmt.shortcuts import *

N = 8

chess_map = [[0 for j in range(N)] for i in range(N)]

vars = {"x{}{}".format(i, j): Symbol("x{}{}".format(i, j), BOOL) for i in range(N) for j in range(N)}
s = Solver()

# No 2 queens attack the same row
for i in range(N):
    s.add_assertion(ExactlyOne(vars["x{}{}".format(i, j)] for j in range(N)))

# No 2 queens attack the same column
for j in range(N):
    s.add_assertion(ExactlyOne(vars["x{}{}".format(i, j)] for i in range(N)))

# No 2 queens attack the same diagonal
# Left-to-right diagonal
s.add_assertion(ExactlyOne(vars["x{}{}".format(i, j)] for i, j in zip(range(N), range(N))))
# Right-to-left diagonal
s.add_assertion(ExactlyOne(vars["x{}{}".format(i, j)] for i, j in zip(range(N), range(N - 1, -1, -1))))


if s.solve():
    print("SAT")
    answer = deepcopy(chess_map)
    first_sol = []
    for var in vars:
        if str(s.get_value(vars[var])) == 'True':
            first_sol.append(vars[var])
            answer[int(var[1])][int(var[2])] = "x"
        else:
            answer[int(var[1])][int(var[2])] = "o"
    for r in answer:
        for e in r:
            print(e, end="  ")
        print("")
    s.push()
    first_sol = And(first_sol)
    s.add_assertion(Not(first_sol))
    if s.solve():
        print("The solution is not unique")
        print("2nd solution:")
        answer = deepcopy(chess_map)
        for var in vars:
            if str(s.get_value(vars[var])) == 'True':
                answer[int(var[1])][int(var[2])] = "x"
            else:
                answer[int(var[1])][int(var[2])] = "o"
        for r in answer:
            for e in r:
                print(e, end="  ")
            print("")
    else:
        print("The solution is unique")
else:
    print("UNSAT")
