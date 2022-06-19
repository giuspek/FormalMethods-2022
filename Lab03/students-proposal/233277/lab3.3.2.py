from pysmt.shortcuts import *

vars = {"{}{}".format(coor, varname): Symbol("{}{}".format(coor, varname), REAL) for coor in "xy" for varname in "AB"}

s = Solver(logic="QF_NRA")
formula = []

s.add_assertion(Equals(vars["xA"], Real(1)))
s.add_assertion(Equals(vars["xB"], Real(2)))
s.add_assertion(Equals(vars["yA"], Real(3)))
s.add_assertion(Equals(vars["yB"], Real(7)))
formula.append(Equals(vars["xA"], Real(1)))
formula.append(Equals(vars["xB"], Real(2)))
formula.append(Equals(vars["yA"], Real(3)))
formula.append(Equals(vars["yB"], Real(7)))


# Line pass through A & B: y = mx + q 
vars["m"] = Symbol("m", REAL)
vars["q"] = Symbol("q", REAL)

# m = (yB - yA) / (xB - xA)
s.add_assertion(Equals(vars["m"], Div(Minus(vars["yB"], vars["yA"]), Minus(vars["xB"], vars["xA"]))))
formula.append(Equals(vars["m"], Div(Minus(vars["yB"], vars["yA"]), Minus(vars["xB"], vars["xA"]))))
# q = yA - m * xA
s.add_assertion(Equals(vars["q"], Minus(vars["yA"], Times(vars["m"], vars["xA"]))))
formula.append(Equals(vars["q"], Minus(vars["yA"], Times(vars["m"], vars["xA"]))))

# Intersection with Ox: 0 = mx_0 + q => x_0 = -q / m
vars["x0"] = Symbol("x0", REAL)
s.add_assertion(Equals(vars["x0"], Div(Minus(Real(0), vars["q"]), vars["m"])))
formula.append(Equals(vars["x0"], Div(Minus(Real(0), vars["q"]), vars["m"])))

formula = And(formula)
write_smtlib(formula, 'lab3.3.2.v2.smt2')

if s.solve():
    print("SAT")
    # Why s.get_value here return FNode, not value of Symbol?
    print("The line pass through A and B is: y = ({})x + ({})".format(s.get_value(vars["m"]), s.get_value(vars["q"])))
    print("The intersection point of the line and the x-axis is: ({}, 0)".format(s.get_value(vars["x0"])))
else:
    print("UNSAT")
