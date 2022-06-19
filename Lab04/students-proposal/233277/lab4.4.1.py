from pysmt.shortcuts import *

vars = {"{}".format(char): Symbol("{}".format(char), BVType(32)) for char in "abc"}

s = Solver()

# assert(isMultiple(a,5))
s.add_assertion(Equals(BVURem(vars["a"], BV(5, 32)), BVZero(32)))

# assert(or(a,b) == 2022))
s.add_assertion(Equals(BVOr(vars["a"], vars["b"]), BV(2022, 32)))

# assert(a - b > 1000)
s.add_assertion(BVUGT(BVSub(vars["a"], vars["b"]), BV(1000, 32)))

# assert(isAverage(c, [a,b]))
s.add_assertion(Equals(BVMul(vars["c"], BV(2, 32)), BVAdd(vars["a"], vars["b"])))

# assert(c<0x76543210)
# Conver 0x76543210 to binary: 0b1110110010101000011001000010000
s.add_assertion(BVULT(vars["c"], BV("#b01110110010101000011001000010000", 32)))
# s.add_assertion(BVULT(vars["c"], BV("#x076543210", 32)))

if s.solve():
    print("SAT")
    print("a = {:032b} ({})".format(int(str(s.get_value(BVToNatural(vars["a"])))), s.get_value(vars["a"])))
    print("b = {:032b} ({})".format(int(str(s.get_value(BVToNatural(vars["b"])))), s.get_value(vars["b"])))
    print("c = {:032b} ({})".format(int(str(s.get_value(BVToNatural(vars["c"])))), s.get_value(vars["c"])))
    print("Password = {:096b} ({})".format(int(str(s.get_value((BVToNatural(BVConcat(BVConcat(vars["a"], vars["b"]), vars["c"])))))), s.get_value((BVConcat(BVConcat(vars["a"], vars["b"]), vars["c"])))))
else:
    print("UNSAT")