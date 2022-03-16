from pysmt.shortcuts import *

msat = Solver()
formula = []
vars = {"x{}{}".format(i,j): Symbol("x{}{}".format(i,j), BOOL) for i in "abcde" for j in range(1,6)}

# Each guest is assigned exactly one room
for i in "abcde":
	msat.add_assertion(ExactlyOne([vars["x{}{}".format(i,j)] for j in range(1,6)]))
	formula.append(ExactlyOne([vars["x{}{}".format(i,j)] for j in range(1,6)]))

# Each room is assigned to exactly one person
for j in range(1,6):
	msat.add_assertion(ExactlyOne([vars["x{}{}".format(i,j)] for i in "abcde"]))
	formula.append(ExactlyOne([vars["x{}{}".format(i,j)] for i in "abcde"]))

guests_conditions = [
					Or(vars["xa1"], vars["xa2"]),
					Or(vars["xb2"], vars["xb4"]),
					vars["xc1"],
					Or(vars["xd2"], vars["xd4"]),
					Or(vars["xe1"], vars["xe5"]),
					]

formula = And(formula)
write_smtlib(formula, "reserve.smt2")
for i in range(len(guests_conditions)):
	msat.push()
	msat.add_assertion(guests_conditions[i])
	res = msat.solve()
	if res:
		pass
	else:
		print("We can satisfy in order {} people".format(i))
		exit()

