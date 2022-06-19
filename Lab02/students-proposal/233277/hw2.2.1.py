from pysmt.shortcuts import *
from copy import deepcopy

sudoku_map = [
    [0, 0, 5, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 4, 9, 2, 0, 0, 0],
    [9, 0, 0, 0, 0, 0, 0, 0, 3],
    [0, 3, 0, 0, 0, 0, 0, 6, 0],
    [0, 9, 0, 0, 0, 0, 0, 1, 0],
    [0, 2, 0, 0, 0, 0, 0, 7, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 0, 6, 8, 7, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 0, 0, 4]
]

# sudoku_map = [
#     [0, 0, 1, 0, 0, 2, 0, 0, 5],
#     [0, 7, 0, 0, 3, 0, 0, 4, 0],
#     [5, 0, 0, 9, 0, 0, 7, 0, 0],
#     [3, 0, 0, 1, 0, 0, 5, 0, 9],
#     [0, 5, 0, 0, 9, 0, 0, 1, 0],
#     [6, 0, 9, 0, 0, 3, 0, 0, 7],
#     [4, 0, 3, 0, 0, 8, 0, 0, 1],
#     [0, 8, 0, 0, 1, 0, 0, 5, 0],
#     [1, 0, 0, 3, 0, 0, 8, 0, 0]
# ]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
vars = {"x{}{}{}".format(i, j, val): Symbol("x{}{}{}".format(i, j, val), BOOL) for i in range(9) for j in range (9) for val in numbers}

s = Solver()

# 1 value only appears once in a row
for n in numbers:
    for i in range(9):
        s.add_assertion(ExactlyOne(vars["x{}{}{}".format(i, j, n)] for j in range(9)))

# 1 value only appears once in a column
for n in numbers:
    for j in range(9):
        s.add_assertion(ExactlyOne(vars["x{}{}{}".format(i, j, n)] for i in range(9)))

# 1 value only appears once in a 3x3 grid
for n in numbers:
    for i in range(3):
        for j in range(3):
            row_start = i * 3
            col_start = j * 3
            s.add_assertion(ExactlyOne(vars["x{}{}{}".format(r, c, n)] for r in range(row_start, row_start + 3) for c in range(col_start, col_start + 3)))

# 1 value for each blank box
for i in range(9):
    for j in range(9):
        if sudoku_map[i][j] == 0:
            s.add_assertion(ExactlyOne(vars["x{}{}{}".format(i, j, n)] for n in numbers))
        else:
            s.add_assertion(vars["x{}{}{}".format(i, j, sudoku_map[i][j])])

# 1 value can appears once in a diagonal
# Left-to-right diagonal
for val in numbers:
    s.add_assertion(ExactlyOne(vars["x{}{}{}".format(i, j, val)] for i, j in zip(range(9), range(9))))
# Right-to-left diagonal
for val in numbers:
    s.add_assertion(ExactlyOne(vars["x{}{}{}".format(i, j, val)] for i, j in zip(range(9), range(8, -1, -1))))


if s.solve():
    print("SAT")
    answer = deepcopy(sudoku_map)
    for var in vars:
        if str(s.get_value(vars[var])) == 'True':
            answer[int(var[1])][int(var[2])] = int(var[3])
    for r in answer:
        print(r)
else:
    print("UNSAT")
    