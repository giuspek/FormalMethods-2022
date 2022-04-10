"""
Model 1: D E A C B
Model 2: D A E C B
Model 3: D A C E B
"""

from pysmt.shortcuts import *
from pysmt.solvers.msat import MathSAT5Solver

a = Symbol("A", INT)
b = Symbol("B", INT)
c = Symbol("C", INT)
d = Symbol("D", INT)
e = Symbol("E", INT)

with Solver() as msat:
    msat: MathSAT5Solver

    # We can execute A after D is completed.
    msat.add_assertion(a > d)

    # We can execute B after C and E are completed.
    msat.add_assertion(b > c)
    msat.add_assertion(b > e)

    # We can execute E after B or D are completed.
    msat.add_assertion((e > b) | (e > d))

    # We can execute C after A is completed.
    msat.add_assertion(c > a)

    # Hidden conditions
    for task in [a, b, c, d, e]:
        # msat.add_assertion(1 <= task <= 5) valid syntax but does not work
        msat.add_assertion(task >= 1)
        msat.add_assertion(task <= 5)
    msat.add_assertion(AllDifferent(a, b, c, d, e))

    n_models = 0
    while msat.solve():
        n_models += 1
        print(f"Model {n_models}:")
        print(msat.get_model())
        partial_model = [Equals(task, msat.get_value(task)) for task in [a, b, c, d, e]]
        msat.add_assertion(Not(And(partial_model)))
