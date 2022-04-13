from pysmt.shortcuts import *
from enum import Enum

'''
Kakuro is a puzzle in which one must put the numbers 1 to 9 in the different cells such that they satisfy certain constraints. 
If a clue is present in a row or column, the sum of the cell for that row should be equal to the value. 
Within each sum all the numbers have to be different, so to add up to 4 we can have 1+3 or 3+1. 
Can we find a solution using SMT solvers?
'''

'''
x  9  34 4  x  
9  D  D  D  x
13 D  D  D  x
13 D  D  11 3
x  7  D  D  D
x  19 D  D  D
'''
class CellType(Enum):
  CONSTRAINT=0
  EMPTY=1
  NUMBER=2

class Cell():
  def __init__(self, cellType, row_c=0, column_c=0):
    self.cellType = cellType
    self.row_c = row_c
    self.column_c = column_c

kakuro_map = [
    [Cell(CellType.EMPTY), Cell(CellType.EMPTY), Cell(CellType.EMPTY), Cell(CellType.CONSTRAINT,0,23), Cell(CellType.CONSTRAINT, 0,4)],
    [Cell(CellType.EMPTY), Cell(CellType.EMPTY), Cell(CellType.CONSTRAINT,9,6), Cell(CellType.NUMBER), Cell(CellType.NUMBER)],
    [Cell(CellType.EMPTY), Cell(CellType.CONSTRAINT,10,4), Cell(CellType.NUMBER), Cell(CellType.NUMBER), Cell(CellType.NUMBER)],
    [Cell(CellType.CONSTRAINT,14,0), Cell(CellType.NUMBER), Cell(CellType.NUMBER), Cell(CellType.NUMBER), Cell(CellType.EMPTY)],
    [Cell(CellType.CONSTRAINT,4,0), Cell(CellType.NUMBER), Cell(CellType.NUMBER), Cell(CellType.EMPTY), Cell(CellType.EMPTY)]
]

row_spaces = [0, 1, 1, 1, 1]
column_spaces = [0, 1, 1, 1, 1]

vars = {}
#i è la riga, j la colonna
for i in range(0, len(kakuro_map)):
    for j in range(0, len(kakuro_map[0])):
        if(kakuro_map[i][j].cellType == CellType.NUMBER):
            vars[f"x{i}{j}"] = Symbol(f"x{i}{j}", INT)


msat = Solver()


assert_row_sums = {}
row_cells_to_sum = {}
#itera sulle righe e fai assert per le somme
for i in range(1, len(kakuro_map)):
    row_cells_to_sum[i] = []
    assert_row_sums[i] = []
    k = -1
    for j in range(0, len(kakuro_map[0])):
        if(kakuro_map[i][j].cellType == CellType.CONSTRAINT and kakuro_map[i][j].row_c != 0):
            k+=1
            if(k>=row_spaces[i]):
                break
            assert_row_sums[i].append(kakuro_map[i][j].row_c)
            row_cells_to_sum[i].append([])
        if(kakuro_map[i][j].cellType == CellType.NUMBER):
            row_cells_to_sum[i][k].append(vars[f"x{i}{j}"])

for i in range(1, len(kakuro_map)):
    for k in range(row_spaces[i]):
        msat.add_assertion(Equals(Int(assert_row_sums[i][k]), Plus(row_cells_to_sum[i][k])))
        msat.add_assertion(AllDifferent(row_cells_to_sum[i][k]))


assert_column_sums = {}
column_cells_to_sum = {}
#itera sulle righe e fai assert per le somme
for j in range(1, len(kakuro_map[0])):
    column_cells_to_sum[j] = []
    assert_column_sums[j] = []
    k = -1
    for i in range(0, len(kakuro_map)):
        if(kakuro_map[i][j].cellType == CellType.CONSTRAINT and kakuro_map[i][j].column_c != 0):
            k+=1
            if(k>=column_spaces[j]):
                break
            assert_column_sums[j].append(kakuro_map[i][j].column_c)
            column_cells_to_sum[j].append([])
        if(kakuro_map[i][j].cellType == CellType.NUMBER):
            column_cells_to_sum[j][k].append(vars[f"x{i}{j}"])

for i in range(1, len(kakuro_map[0])):
    for k in range(column_spaces[i]):
        msat.add_assertion(Equals(Int(assert_column_sums[i][k]), Plus(column_cells_to_sum[i][k])))
        msat.add_assertion(AllDifferent(column_cells_to_sum[i][k]))


for i in range(1, len(kakuro_map)):
    for j in range(0, len(kakuro_map[0])):
        if(kakuro_map[i][j].cellType == CellType.NUMBER):
            msat.add_assertion(LT(vars[f"x{i}{j}"], Int(10)))
            msat.add_assertion(GT(vars[f"x{i}{j}"], Int(0)))


res = msat.solve()


if res:
    solution = list()
    print("SAT")
    sat_model = {el[0].symbol_name():el[1] for el in msat.get_model()}
    for i in range(len(kakuro_map)):
      row = list()
      for j in range(len(kakuro_map[0])):
        if(kakuro_map[i][j].cellType == CellType.EMPTY):
          row.append("x ")
        if(kakuro_map[i][j].cellType == CellType.NUMBER):
          row.append("{} ".format(sat_model[f"x{i}{j}"]))
        if(kakuro_map[i][j].cellType == CellType.CONSTRAINT):
          row.append(f"c{kakuro_map[i][j].column_c}-{kakuro_map[i][j].row_c}")

      solution.append(row)
    
    for line in solution:
      print(line)
else:
    print("UNSAT")