from pysmt.shortcuts import *
from pysmt.solvers.msat import MathSAT5Solver

var = {f"x{i}{j}": Symbol(f"x{i}{j}") for i in "abcde" for j in range(1, 6)}

with Solver() as msat:
	msat: MathSAT5Solver

	# Each guest is assigned exactly one room
	for i in "abcde":
		msat.add_assertion(ExactlyOne([var[f"x{i}{j}"] for j in range(1, 6)]))

	# Each room is assigned to exactly one person
	for j in range(1, 6):
		msat.add_assertion(ExactlyOne([var[f"x{i}{j}"] for i in "abcde"]))

	write_smtlib(And(msat.assertions), "reserve.smt2")

	guests_conditions = [
		Or(var["xa1"], var["xa2"]),  # Guest A would like to choose room 1 or 2.
		Or(var["xb2"], var["xb4"]),  # Guest B would like to choose a room with an even number.
		var["xc1"],  # Guest C would like the first room.
		Or(var["xd2"], var["xd4"]),  # Guest D has the same behaviour as user B.
		Or(var["xe1"], var["xe5"]),  # Guest E would like one of the external rooms.
	]

	for i, condition in enumerate(guests_conditions):
		msat.push()
		msat.add_assertion(condition)
		if not msat.solve():
			print(f"We can satisfy in order {i} guests out of {len(guests_conditions)}")
			break
