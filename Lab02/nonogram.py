from pysmt.shortcuts import *

# Number k is in position (i,j)
msat = Solver()

ancillas_index = 1
nonogram_column_hints = [2,3,4,2,2]
nonogram_row_hints = [2,3,3,(3,1),1]
nonogram_size = (len(nonogram_row_hints), len(nonogram_column_hints))
vars = {"x{}{}".format(i,j): Symbol("x{}{}".format(i,j), BOOL) for i in range(len(nonogram_row_hints)) for j in range(len(nonogram_column_hints))}

def encode_one(index, ctype):
	global ancillas_index
	size = nonogram_size[0] if ctype == "r" else nonogram_size[1] 
	list_of_or = []
	for i in range(0, size-1+1):
		ancilla = Symbol("a{}".format(ancillas_index), BOOL)
		ancillas_index += 1
		if ctype == "r":
			list_of_or.append(And([vars["x{}{}".format(index, i%size)] for i in range(i, i+1)]+[Not(vars["x{}{}".format(index, i%size)]) for i in range(i+1, i+size)]))	
		else:
			list_of_or.append(And([vars["x{}{}".format(i%size, index)] for i in range(i, i+1)]+[Not(vars["x{}{}".format(i%size, index)]) for i in range(i+1, i+size)]))	
	msat.add_assertion(Or(list_of_or))

def encode_two(index, ctype):
	global ancillas_index
	size = nonogram_size[0] if ctype == "r" else nonogram_size[1] 
	list_of_or = []
	for i in range(0, size-2+1):
		ancilla = Symbol("a{}".format(ancillas_index), BOOL)
		ancillas_index += 1
		if ctype == "r":
			list_of_or.append(And([vars["x{}{}".format(index, i%size)] for i in range(i, i+2)]+[Not(vars["x{}{}".format(index, i%size)]) for i in range(i+2, i+size)]))	
		else:
			list_of_or.append(And([vars["x{}{}".format(i%size, index)] for i in range(i, i+2)]+[Not(vars["x{}{}".format(i%size, index)]) for i in range(i+2, i+size)]))	
	msat.add_assertion(Or(list_of_or))

def encode_three(index, ctype):
	global ancillas_index
	size = nonogram_size[0] if ctype == "r" else nonogram_size[1] 
	list_of_or = []
	for i in range(0, size-3+1):
		ancilla = Symbol("a{}".format(ancillas_index), BOOL)
		ancillas_index += 1
		if ctype == "r":
			list_of_or.append(And([vars["x{}{}".format(index, i%size)] for i in range(i, i+3)]+[Not(vars["x{}{}".format(index, i%size)]) for i in range(i+3, i+size)]))
		else:
			list_of_or.append(And([vars["x{}{}".format(i%size, index)] for i in range(i, i+3)]+[Not(vars["x{}{}".format(i%size, index)]) for i in range(i+3, i+size)]))	
	msat.add_assertion(Or(list_of_or))

def encode_three_one(index, ctype):
	if ctype == "r":
		msat.add_assertion(And(vars["x{}{}".format(index, 0)], vars["x{}{}".format(index, 1)], vars["x{}{}".format(index, 2)], Not(vars["x{}{}".format(index, 3)]), vars["x{}{}".format(index, 4)]))
	else:
		msat.add_assertion(And(vars["x{}{}".format(0, index)], vars["x{}{}".format(1, index)], vars["x{}{}".format(2, index)], Not(vars["x{}{}".format(3, index)]), vars["x{}{}".format(4, index)]))

def encode_four(index, ctype):
	global ancillas_index
	size = nonogram_size[0] if ctype == "r" else nonogram_size[1] 
	list_of_or = []
	for i in range(0, size-4+1):
		ancilla = Symbol("a{}".format(ancillas_index), BOOL)
		ancillas_index += 1
		if ctype == "r":
			list_of_or.append(And([vars["x{}{}".format(index, i%size)] for i in range(i, i+4)]+[Not(vars["x{}{}".format(index, i%size)]) for i in range(i+4, i+size)]))	
		else:
			list_of_or.append(And([vars["x{}{}".format(i%size, index)] for i in range(i, i+4)]+[Not(vars["x{}{}".format(i%size, index)]) for i in range(i+4, i+size)]))
	msat.add_assertion(Or(list_of_or))


for i in range(len(nonogram_row_hints)):
	hint = nonogram_row_hints[i]
	if hint == 2:
		encode_two(i, "r")
	if hint == 3:
		encode_three(i, "r")
	if hint == 4:
		encode_four(i, "r")
	if hint == (3,1):
		encode_three_one(i, "r")
	if hint == 1:
		encode_one(i, "r")

for i in range(len(nonogram_column_hints)):
	hint = nonogram_column_hints[i]
	if hint == 2:
		encode_two(i, "c")
	if hint == 3:
		encode_three(i, "c")
	if hint == 4:
		encode_four(i, "c")
	if hint == (3,1):
		encode_three_one(i, "c")
	if hint == 1:
		encode_one(i, "c")

res = msat.solve()
if res:
	solution = list()
	sat_model = {el[0].symbol_name():el[1] for el in msat.get_model()}
	for i in range(0,nonogram_size[0]):
		row = ""
		for j in range(0,nonogram_size[1]):
			if sat_model["x{}{}".format(i,j)] == Bool(True):
				row += "*"
			else:
				row += " "
		solution.append(row)
	for line in solution:
		print(line)
else:
	print("UNSAT")