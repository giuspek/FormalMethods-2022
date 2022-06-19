from pysmt.shortcuts import *

vars = {"{}".format(char): Symbol("{}".format(char), INT) for char in "abc"}

s = Solver()

# a can pick 1 value from 1 to 9
s.add_assertion(And(LE(vars["a"], Int(9)), GE(vars["a"], Int(1))))

# b can pick 1 value from 0 to 9
s.add_assertion(And(LE(vars["b"], Int(9)), GE(vars["b"], Int(0))))

# c can pick 1 value from 1 to 9
s.add_assertion(And(LE(vars["c"], Int(9)), GE(vars["c"], Int(1))))

# abc is multiples of 4
abc = Plus(Times(vars["a"], Int(100)), Times(vars["b"], Int(10)), vars["c"])
vars["r1"] = Symbol("r1", INT)
s.add_assertion(Equals(Times(vars["r1"], Int(4)), abc))

# cba is multiples of 4
cba = Plus(Times(vars["c"], Int(100)), Times(vars["b"], Int(10)), vars["a"])
vars["r2"] = Symbol("r2", INT)
s.add_assertion(Equals(Times(vars["r2"], Int(4)), cba))

num_sol = 0
solutions = []
while s.solve():
    num_sol += 1
    solutions.append(int(str(s.get_value(vars["a"])) + str(s.get_value(vars["b"])) + str(s.get_value(vars["c"]))))
    s.push()
    formula = And(Equals(vars["{}".format(char)], s.get_value(vars["{}".format(char)])) for char in "abc")
    s.add_assertion(Not(formula))
print("There are in total {} positive integers satisfying the given constraint: \n{}".format(num_sol, sorted(solutions)))

