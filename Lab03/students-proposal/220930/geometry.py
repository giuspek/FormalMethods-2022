"""
geometry.smt
sat
(model
  (define-fun xa () Real (to_real 1))
  (define-fun ya () Real (to_real 3))
  (define-fun xb () Real (to_real 2))
  (define-fun yb () Real (to_real 7))
  (define-fun x () Real (/ 1 4))
  (define-fun m () Real (to_real 4))
  (define-fun q () Real (to_real (- 1)))
)

geometry.py
q := -1.0
x := 1/4
m := 4.0
Xa := 1.0
Ya := 3.0
Xb := 2.0
Yb := 7.0
"""

from pysmt.shortcuts import *
from pysmt.solvers.msat import MathSAT5Solver

xa = Symbol("Xa", REAL)
ya = Symbol("Ya", REAL)
xb = Symbol("Xb", REAL)
yb = Symbol("Yb", REAL)

x = Symbol("x", REAL)
m = Symbol("m", REAL)
q = Symbol("q", REAL)

f = Symbol("f", FunctionType(REAL, (REAL,)))

with Solver() as msat:
    msat: MathSAT5Solver

    # This produces the following exception:
    # pysmt.exceptions.NonLinearError: (m * (Xb - Xa))
    # To bypass the exception, edit the "walk_times" function in pysmt/solvers as follows:
    # def walk_times(self, formula, args, **kwargs):
    #     res = args[0]
    #     nl_count = 0 if mathsat.msat_term_is_number(self.msat_env(), res) else 1
    #     for x in args[1:]:
    #         res = mathsat.msat_make_times(self.msat_env(), res, x)
    #     return res
    msat.add_assertion(Equals(f(x), Plus(Times(m, x), q)))

    msat.add_assertion(Equals(xa, Real(1)))
    msat.add_assertion(Equals(ya, Real(3)))
    msat.add_assertion(Equals(xb, Real(2)))
    msat.add_assertion(Equals(yb, Real(7)))

    # This produces the following exception:
    # pysmt.exceptions.ConvertExpressionError: Could not convert the input expression.
    # The formula contains unsupported operators. The error was: Unsupported operator 'DIV' (node_type: 62)
    # msat.add_assertion(Equals(m, Div((Minus(yb, ya)), Minus(xb, xa))))
    # This works:
    # msat.add_assertion(Equals(Times(m, Minus(xb, xa)), Minus(yb, ya)))
    msat.add_assertion(Equals(m * (xb - xa), yb - ya))

    # msat.add_assertion(Equals(q, Minus(yb, Times(m, xb))))
    msat.add_assertion(Equals(q, yb - m * xb))

    # msat.add_assertion(Equals(Function(f, [x]), Real(0)))
    msat.add_assertion(Equals(f(x), Real(0)))

    if msat.solve():
        print(msat.get_model())
    else:
        print("UNSAT")
