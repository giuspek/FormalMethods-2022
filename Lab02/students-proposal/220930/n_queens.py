import time

from pysmt.shortcuts import *
from pysmt.solvers.msat import MathSAT5Solver, MathSAT5Model

N = 8


def print_model(model: MathSAT5Model):
	rows = []

	for i in range(0, N):
		row = []
		for j in range(0, N):
			if model.get_py_value(var[f"x{i}{j}"]):
				row.append("♛")
			else:
				row.append(" ")
		rows.append(row)

	rows.insert(0, [" "])
	for j in range(N):
		rows[0].append(str(j))
	for i in range(1, N + 1):
		rows[i].insert(0, str(i))

	for row in rows:
		print(row)


with Solver() as msat:
	msat: MathSAT5Solver

	var = {}
	for n_solutions in range(0, N):
		for j in range(0, N):
			var[f"x{n_solutions}{j}"] = Symbol(f"x{n_solutions}{j}")

	for n_solutions in range(0, N):
		row = [var[f"x{n_solutions}{j}"] for j in range(N)]
		# print(f"Row {n_solutions}: {row}")
		msat.add_assertion(ExactlyOne(row))

	for j in range(0, N):
		col = [var[f"x{i}{j}"] for i in range(N)]
		# print(f"Col {j}: {col}")
		msat.add_assertion(ExactlyOne(col))

	# credit: https://stackoverflow.com/a/54334786
	for p in range(2 * N - 1):
		diag = [var[f"x{p - q}{q}"] for q in range(max(0, p - N + 1), min(p, N - 1) + 1)]
		# print(f"↗: {diag}")
		msat.add_assertion(AtMostOne(diag))

		diag = [var[f"x{N - p + q - 1}{q}"] for q in range(max(0, p - N + 1), min(p, N - 1) + 1)]
		# print(f"↘: {diag}")
		msat.add_assertion(AtMostOne(diag))

	initial_time = time.time()

	n_solutions = 0
	while msat.solve():
		n_solutions += 1
		# print(f"Solution #{n_solutions}:")
		# print_model(msat.get_model())

		# msat.print_model() # TypeError: object of type 'FNode' has no len()
		# msat.print_model(f) # NotImplementedError

		# partial truth assignment
		true_literals = And(literal for literal, _ in msat.get_model() if msat.get_py_value(literal))
		msat.add_assertion(Not(true_literals))

	print(f"Found {n_solutions} solutions")
	print(f"elapsed time: {time.time() - initial_time}")
