from pysmt.shortcuts import *

nonogram_map = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

vars = {"x{}{}".format(i, j): Symbol("x{}{}".format(i, j), BOOL) for i in range(5) for j in range(5)}

s = Solver()

# last row
s.add_assertion(ExactlyOne(vars["x4{}".format(j)] for j in range(5)))

# 4th row
for j in range(3):
    s.add_assertion(vars["x3{}".format(j)])
s.add_assertion(Not(vars["x33"]))
s.add_assertion(vars["x34"])

# other rows
cols_constraint = [2, 3, 4, 2, 2]
rows_constraint = [2, 3, 3]

# columns constraint
for j, c in enumerate(cols_constraint):
    s.add_assertion(ExactlyOne(And(*[vars["x{}{}".format(i + x, j)] for x in range(c)], Not(Or(vars["x{}{}".format(k, j)] for k in range(5) if k not in [i + x for x in range(c)]))) for i in range(5 - c + 1)))

# rows constraint
for i, c in enumerate(rows_constraint):
    s.add_assertion(ExactlyOne(And(*[vars["x{}{}".format(i, j + x)] for x in range(c)], Not(Or(vars["x{}{}".format(i, k)] for k in range(5) if k not in [j + x for x in range(c)]))) for j in range(5 - c + 1)))

if s.solve():
    print("SAT")
    for var in vars:
        if str(s.get_value(vars[var])) == 'True':
            nonogram_map[int(var[1])][int(var[2])] = 'x'
        else:
            nonogram_map[int(var[1])][int(var[2])] = 'o'
    for r in nonogram_map:
        for e in r:
            print(e, end="  ")
        print("")
else:
    print("UNSAT")
    


