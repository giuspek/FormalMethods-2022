"""
Minimum reproducible example of solver stuck in a loop with ForAll and Iff
"""

from pysmt.shortcuts import *
from pysmt.solvers.z3 import Z3Solver

i = Symbol("i", INT)
j = Symbol("j", INT)

richer = Symbol("richer", FunctionType(BOOL, [INT, INT]))

with Solver(name="z3") as solver:
    solver: Z3Solver

    solver.add_assertion(ForAll([i, j], Implies(NotEquals(i, j), Iff(richer(i, j), Not(richer(j, i))))))

    if solver.solve():
        print(solver.get_model())

    # Unreachable
    print("Done")
