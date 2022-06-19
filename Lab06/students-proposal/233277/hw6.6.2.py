from pysmt.shortcuts import *

vars = {"x{}{}".format(i, char): Symbol("x{}{}".format(i, char), INT) for i in range(1, 11) for char in "AB"}

s = Solver()

# 1 question can only reward 10 or 0 by choosing A or B
for i in range(1, 11):
    s.add_assertion(ExactlyOne(Equals(vars["x{}A".format(i)], Int(10)), Equals(vars["x{}B".format(i)], Int(10))))
    s.add_assertion(ExactlyOne(Equals(vars["x{}A".format(i)], Int(0)), Equals(vars["x{}B".format(i)], Int(0))))

# If A is true then B is false and vice versa
for i in range(1, 11):
    s.add_assertion(Implies(Equals(vars["x{}A".format(i)], Int(10)), Equals(vars["x{}B".format(i)], Int(0))))
    s.add_assertion(Implies(Equals(vars["x{}B".format(i)], Int(10)), Equals(vars["x{}A".format(i)], Int(0))))
    s.add_assertion(Implies(Equals(vars["x{}A".format(i)], Int(0)), Equals(vars["x{}B".format(i)], Int(10))))
    s.add_assertion(Implies(Equals(vars["x{}B".format(i)], Int(0)), Equals(vars["x{}A".format(i)], Int(10))))

# Mary's mark
s.add_assertion(Equals(Plus(vars["x1B"], vars["x2B"], vars["x3A"], vars["x4B"], vars["x5A"], vars["x6B"], vars["x7B"], vars["x8A"], vars["x9B"], vars["x10B"]), Int(70)))

# Dan's mark
s.add_assertion(Equals(Plus(vars["x1B"], vars["x2A"], vars["x3A"], vars["x4A"], vars["x5B"], vars["x6A"], vars["x7B"], vars["x8A"], vars["x9A"], vars["x10A"]), Int(50)))

# Lisa's mark
s.add_assertion(Equals(Plus(vars["x1B"], vars["x2A"], vars["x3A"], vars["x4A"], vars["x5B"], vars["x6B"], vars["x7B"], vars["x8A"], vars["x9B"], vars["x10A"]), Int(30)))

vars["Johns_mark"] = Symbol("Johns_mark", INT)
s.add_assertion(Equals(Plus(vars["x1B"], vars["x2B"], vars["x3A"], vars["x4A"], vars["x5A"], vars["x6B"], vars["x7B"], vars["x8A"], vars["x9A"], vars["x10A"]), vars["Johns_mark"]))

if s.solve():
    print("SAT")
    johns_mark = int(str(s.get_value(vars["Johns_mark"])))
    print("John's mark: {}".format(johns_mark))
    s.push()
    s.add_assertion(Not(Equals(vars["Johns_mark"], Int(johns_mark))))
    if s.solve():
        print("Solution is not unique")
        johns_mark = int(str(s.get_value(vars["Johns_mark"])))
        print("Alternative solution: {}".format(johns_mark))
    else:
        print("Solution is unique")
else:
    print("UNSAT")







