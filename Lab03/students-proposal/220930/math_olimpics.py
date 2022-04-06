import time

from pysmt.shortcuts import *
from pysmt.solvers.msat import MathSAT5Solver

a = Symbol("A", INT)
b = Symbol("B", INT)
c = Symbol("C", INT)

h = Symbol("h", INT)
k = Symbol("k", INT)

with Solver() as msat:
    msat: MathSAT5Solver

    # msat.add_assertion(GT(a, Int(0)))
    msat.add_assertion((a > 0) & (a <= 9))

    # msat.add_assertion(GE(b, Int(0)))
    msat.add_assertion((b >= 0) & (b <= 9))

    # msat.add_assertion(GT(c, Int(0)))
    msat.add_assertion((c > 0) & (c <= 9))

    # abc = Plus(Times(Int(100), a), Times(Int(10), b), c)
    abc = 100 * a + 10 * b + c
    msat.add_assertion(Equals(Times(h, Int(4)), abc))

    # cba = Plus(Times(Int(100), c), Times(Int(10), b), a)
    cba = 100 * c + 10 * b + a
    msat.add_assertion(Equals(Times(k, Int(4)), cba))

    start_time = time.time()

    n_models = 0
    while msat.solve():
        n_models += 1
        print(f"model {n_models}: {msat.get_value(a)}{msat.get_value(b)}{msat.get_value(c)}")

        # Slowest to fastest
        # partial_model = [Equals(key, value) for key, value in msat.get_model()]
        # partial_model = [Equals(key, msat.get_value(key)) for key in [a, b, c, h, k]]
        partial_model = [Equals(key, msat.get_value(key)) for key in [a, b, c]]

        # Both are slow
        # partial_model = [Equals(key, msat.get_value(key)) for key in [h, k]]
        # partial_model = [Equals(key, msat.get_value(key)) for key in [abc, cba]]

        msat.add_assertion(Not(And(partial_model)))

    print(f"elapsed time: {time.time() - start_time}")
