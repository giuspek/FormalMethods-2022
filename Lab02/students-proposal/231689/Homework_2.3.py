from pysmt.shortcuts import *

'''
solve N-queens problem
every queen must not be attacked by any other
for a queen to be attacked means that another queen is in her same row, column or diagonal
variables can be the presence or not of the queen in the cell i,j where i is the row and j is the column
Xij should be exactly on in row, in column and in diagonal
'''

cells = {f"x{i}{j}": Symbol(f"x{i}{j}", BOOL) for i in range (1,9) for j in range (1,9)}

msat = Solver()


for i in range(1,9):
    # Only one queen per row
    msat.add_assertion(ExactlyOne([cells[f"x{i}{j}"] for j in range(1,9)]))
    # Only one queen per column
    msat.add_assertion(ExactlyOne([cells[f"x{j}{i}"] for j in range(1,9)]))

for i in range(1,8):
    # diagonali destre da A a G (7 volte AtMostOne)
    msat.add_assertion(AtMostOne([cells[f"x{j}{i+j-1}"] for j in range(1,10-i)]))
    # diagonali sinistre da H a B (7 volte AtMostOne)
    msat.add_assertion(AtMostOne([cells[f"x{j}{10-(i+j)}"] for j in range(1,10-i)]))

for i in range (2,8):
    # diagonali destre (A) da 2 a 7 (6 volte AtMostOne)
    msat.add_assertion(AtMostOne([cells[f"x{i+j-1}{j}"] for j in range(1,10-i)]))
    # diagonali sinistre (H) da 2 a 7 (6 volte AtMostOne)
    msat.add_assertion(AtMostOne([cells[f"x{j}{8-j+i}"] for j in range(i, 9)]))


res = msat.solve()
row = list()

if res:
    sat_model = {el[0].symbol_name():el[1] for el in msat.get_model()}
    for i in range(1,9):
        for j in range(1,9):
            if sat_model[f"x{i}{j}"] == Bool(True):
                row.append(f"x{i}{j}")
    print("\n".join(row))
else:
    print("UNSAT")