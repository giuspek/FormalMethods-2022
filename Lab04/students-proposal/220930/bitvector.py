"""
mathsat Lab04/bitvector.smt -model
sat
( (a (_ bv2020 32))
  (b (_ bv2 32))
  (c (_ bv1011 32)) )
"""

from pysmt.shortcuts import *
from pysmt.solvers.msat import MathSAT5Solver

# Either use BVType(32), or:
# from pysmt.typing import BV32

a = Symbol("a", BVType(32))
b = Symbol("b", BVType(32))
c = Symbol("c", BVType(32))

bv0 = BVZero(32)
bv5 = BV(5, 32)
bv2022 = BV(2022, 32)
bv1000 = BV(1000, 32)
bv2 = BV(2, 32)
bv_hex = BV(0x76543210, 32)

with Solver() as msat:
    msat: MathSAT5Solver

    msat.add_assertion(Equals(BVURem(a, bv5), bv0))
    msat.add_assertion(Equals(BVOr(a, b), bv2022))
    msat.add_assertion(BVUGT(BVSub(a, b), bv1000))
    msat.add_assertion(Equals(c, BVUDiv(BVAdd(a, b), bv2)))
    msat.add_assertion(BVULT(c, bv_hex))

    if msat.solve():
        key = BVToNatural(BVConcat(msat.get_value(a), msat.get_value(b), msat.get_value(c)))
        print(key)
    else:
        print("UNSAT")
