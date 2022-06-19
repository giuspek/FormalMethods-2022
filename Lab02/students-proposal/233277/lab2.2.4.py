from pysmt.shortcuts import *

guests = ["A", "B", "C", "D", "E"]
rooms = [1, 2, 3, 4, 5]
formula = []
vars = {"x{}{}".format(g, r): Symbol("x{}{}".format(g, r), BOOL) for g in guests for r in rooms}

s = Solver()

# Each guest only 1 room
for g in guests:
    s.add_assertion(ExactlyOne([vars["x{}{}".format(g, r)] for r in rooms]))
    formula.append(ExactlyOne([vars["x{}{}".format(g, r)] for r in rooms]))

# Each room only 1 guest
for r in rooms:
    s.add_assertion(ExactlyOne([vars["x{}{}".format(g, r)] for g in guests]))
    formula.append(ExactlyOne([vars["x{}{}".format(g, r)] for g in guests]))

# Guest A would like to choose room 1 or 2
clause_A = Or(vars["xA1"], vars["xA2"])

# Guest B would like to choose a room with an even number
clause_B = Or(vars["xB{}".format(r)] for r in rooms if r % 2 == 0)

# Guest C would like the first room
clause_C = vars["xC1"]

# Guest D has the same behaviour as user B
clause_D = Or(vars["xD{}".format(r)] for r in rooms if r % 2 == 0)

# Guest E would like one of the external rooms
clause_E = Or(vars["xE1"], vars["xE5"])

# Incremental SAT
clauses = [clause_A, clause_B, clause_C, clause_D, clause_E]

for i, clause in enumerate(clauses):
    s.push()
    s.add_assertion(clause)
    if s.solve():
        pass
    else:
        num_p = i
        if num_p == 0:
            print("We cannot even satisfy the first customer")
            exit()
        elif num_p == 1:
            print("In this order, we can satisfy 1 person")
            exit()
        else:
            print("In this order, we can satisfy {} people".format(num_p))
            exit()
print("In this order, we can satisfy all customers")