"""
guesscode.smt
sat
(model
  (define-fun e () Int 8)
  (define-fun a () Int 2)
  (define-fun b () Int 3)
  (define-fun c () Int 6)
  (define-fun d () Int 8)
)

guesscode.py
C := 6
A := 2
D := 8
B := 3
"""

from pysmt.shortcuts import *
from pysmt.solvers.msat import MathSAT5Solver

a = Symbol("A", INT)
b = Symbol("B", INT)
c = Symbol("C", INT)
d = Symbol("D", INT)

# with Solver(logic="NIA") as msat:
with Solver() as msat:
    msat: MathSAT5Solver

    msat.add_assertion(Equals(d, Plus(a, c)))
    msat.add_assertion(Equals(c, Times(a, b)))
    msat.add_assertion(Equals(b, Minus(c, b)))
    msat.add_assertion(Equals(d, Times(a, Int(4))))

    msat.add_assertion(GE(a, Int(0)))
    msat.add_assertion(LE(a, Int(9)))
    msat.add_assertion(GE(b, Int(0)))
    msat.add_assertion(LE(b, Int(9)))
    msat.add_assertion(GE(c, Int(0)))
    msat.add_assertion(LE(c, Int(9)))
    msat.add_assertion(GE(d, Int(0)))
    msat.add_assertion(LE(d, Int(9)))

    msat.add_assertion(AllDifferent(a, b, c, d))

    if msat.solve():
        model = msat.get_model()
        print(f"{model.get_value(a)}{model.get_value(b)}{model.get_value(c)}{model.get_value(d)}")
    else:
        print("UNSAT")
