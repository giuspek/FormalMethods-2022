from pysmt.shortcuts import *
from copy import deepcopy

# diamond, triangle, circle, pentagon, rectangle (triangle = square / 2)

shapes = ["Diamond", "Triangle", "Circle", "Pentagon", "Rectangle"]
vars = {"{}".format(char): Symbol("{}".format(char), INT) for char in shapes}

formula = []

# diamond + square + circle = pentagon + 2 * rectangle
formula.append(Equals(Plus(vars["Diamond"], Times(vars["Triangle"], Int(2)), vars["Circle"]), Plus(vars["Pentagon"], Times(Int(2), vars["Rectangle"]))))

# square + pentagon = circle + diamond + square => pentagon = circle + diamond
formula.append(Equals(vars["Pentagon"], Plus(vars["Circle"], vars["Diamond"])))

# Without loss of generality, let triangle = 100
formula.append(Equals(Times(vars["Triangle"], Int(2)), Int(100)))

# # Different shapes has different values => UNSAT
# formula.append(AllDifferent(vars["{}".format(sh)] for sh in shapes))


# Unknown value
unk = Times(Int(3), vars["Rectangle"])

# Answer A: unknown = 2 * diamond + square
ans_A = Equals(unk, Plus(Times(Int(2), vars["Diamond"]), Times(vars["Triangle"], Int(2))))

# Answer B: unknown = diamond + square
ans_B = Equals(unk, Plus(vars["Diamond"], Times(vars["Triangle"], Int(2))))

# Answer C: unknown = square + square / 2
ans_C = Equals(unk, Plus(Times(vars["Triangle"], Int(2)), vars["Triangle"]))

# Answer D: unknown = pentagon + diamond
ans_D = Equals(unk, Plus(vars["Pentagon"], vars["Diamond"]))

answers = [ans_A, ans_B, ans_C, ans_D]

formulas = [deepcopy(formula) + [ans] for ans in answers]
formulas = [And(f) for f in formulas]

for f in formulas:
    write_smtlib(f, "hw3.3.2.{}.smt2".format("ABCD"[formulas.index(f)]))
    if is_sat(f):
        print("Solution {}:".format("ABCD"[formulas.index(f)]))
        print(get_model(f))
        print("")