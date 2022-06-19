from pysmt.shortcuts import *

vars = {"{}".format(c): Symbol("{}".format(c), INT) for c in "abcde"}

formula = []

s = Solver(logic="QF_NRA")

# Single digit numbers
for c in "abcd":
    s.add_assertion(And(GE(vars["{}".format(c)], Int(0)), LE(vars["{}".format(c)], Int(9))))
    formula.append(And(GE(vars["{}".format(c)], Int(0)), LE(vars["{}".format(c)], Int(9))))

# Distinct numbers
s.add_assertion(AllDifferent(vars["{}".format(c)] for c in "abcd"))
formula.append(AllDifferent(vars["{}".format(c)] for c in "abcd"))

# a + c = d
s.add_assertion(Equals(Plus(vars["a"], vars["c"]), vars["d"]))
formula.append(Equals(Plus(vars["a"], vars["c"]), vars["d"]))

# a * 4 = d
s.add_assertion(Equals(Times(vars["a"], Int(4)), vars["d"]))
formula.append(Equals(Times(vars["a"], Int(4)), vars["d"]))

# c - b = b
s.add_assertion(Equals(Minus(vars["c"], vars["b"]), vars["b"]))
formula.append(Equals(Minus(vars["c"], vars["b"]), vars["b"]))

# a * b = c
s.add_assertion(Equals(Times(vars["a"], vars["b"]), vars["c"]))
formula.append(Equals(Times(vars["a"], vars["b"]), vars["c"]))

# e = max(a,b,c,d)
s.add_assertion(Equals(vars["e"], Max(vars["{}".format(s)] for s in "abcd")))
formula.append(Equals(vars["e"], Max(vars["{}".format(s)] for s in "abcd")))

formula = And(formula)
write_smtlib(formula, 'lab3.3.1.v2.smt2')

if s.solve():
    print("SAT")
    for c in "abcde":
        print("{} = {}".format(c, s.get_value(vars[c])))
        
else:
    print("UNSAT")