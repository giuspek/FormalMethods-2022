from pysmt.shortcuts import *
from pysmt.solvers.msat import MathSAT5Solver, MSatConverter

x11 = Symbol("x11")
x12 = Symbol("x12")
x13 = Symbol("x13")
x14 = Symbol("x14")
x21 = Symbol("x21")
x22 = Symbol("x22")
x23 = Symbol("x23")
x24 = Symbol("x24")
x31 = Symbol("x31")
x32 = Symbol("x32")
x33 = Symbol("x33")
x34 = Symbol("x34")
x41 = Symbol("x41")
x42 = Symbol("x42")
x43 = Symbol("x43")
x44 = Symbol("x44")

var = [x11, x12, x13, x14,
       x21, x22, x23, x24,
       x31, x32, x33, x34,
       x41, x42, x43, x44]

with Solver() as msat:
    msat: MathSAT5Solver

    # For each step, only one pin can be used

    msat.add_assertion(ExactlyOne(x11, x21, x31, x41))
    msat.add_assertion(ExactlyOne(x12, x22, x32, x42))
    msat.add_assertion(ExactlyOne(x13, x23, x33, x43))
    msat.add_assertion(ExactlyOne(x14, x24, x34, x44))

    # Each pin can be used once

    msat.add_assertion(ExactlyOne(x11, x12, x13, x14))
    msat.add_assertion(ExactlyOne(x21, x22, x23, x24))
    msat.add_assertion(ExactlyOne(x31, x32, x33, x34))
    msat.add_assertion(ExactlyOne(x41, x42, x43, x44))

    # I've written the representation of patterns considering the possible choices instead of aborting unvalid choices;
    # you can write the dual encoding and test their equivalence.

    msat.add_assertion(Implies(x11, Or(x22, x32)))
    msat.add_assertion(Implies(x21, Or(x12, x42)))
    msat.add_assertion(Implies(x31, Or(x12, x42)))
    msat.add_assertion(Implies(x41, Or(x22, x32)))

    msat.add_assertion(Implies(x12, Or(x23, x33)))
    msat.add_assertion(Implies(x22, Or(x13, x43)))
    msat.add_assertion(Implies(x32, Or(x13, x43)))
    msat.add_assertion(Implies(x42, Or(x23, x33)))

    msat.add_assertion(Implies(x13, Or(x24, x34)))
    msat.add_assertion(Implies(x23, Or(x14, x44)))
    msat.add_assertion(Implies(x33, Or(x14, x44)))
    msat.add_assertion(Implies(x43, Or(x24, x34)))

    n_models = 0


    def callback(model, converter: MSatConverter):
        global n_models
        n_models += 1
        py_model = [converter.back(v) for v in model]
        print(f"Model {n_models}: {py_model}")
        return 1


    msat.all_sat(var, lambda model: callback(model, msat.converter))
