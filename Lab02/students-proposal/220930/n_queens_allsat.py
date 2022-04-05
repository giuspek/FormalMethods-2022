import time

import mathsat
from pysmt.shortcuts import *
from pysmt.solvers.msat import MathSAT5Solver

N = 8

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


	def callback():
		global n_solutions
		n_solutions += 1
		return 1


	mathsat.msat_all_sat(msat.msat_env(), [msat.converter.convert(term) for term in var.values()], lambda _: callback())
	# msat.all_sat(var.values(), lambda _: callback())

	print(f"elapsed time: {time.time() - initial_time}")
