from pysmt.shortcuts import *

# Support variables for readibility
n = 3
agatha = Int(0)
butler = Int(1)
charles = Int(2)

victim = agatha

solver = Solver(name="z3")

who = ["agatha","butler","charles"]

killer = Symbol("killer", INT)

fu = FunctionType(BOOL, [INT, INT])

hates = Symbol("hates", fu)
richer = Symbol("richer", fu)
i = Symbol('i', INT)
j = Symbol('j', INT)

# Agatha, the butler, and Charles live in Dreadsbury Mansion, and 
# are the only ones to live there. 
solver.add_assertion(And(GE(killer,agatha), LE(killer,charles)))

# A killer always hates, and is no richer than his victim. 
solver.add_assertion(Function(hates, [killer,victim]))
solver.add_assertion(Not(Function(richer, [killer,victim])))


# Hidden condition: no one is richer than him-/herself (non-reflexivity)
solver.add_assertion(ForAll([i], Not(Function(richer, [i,i]))))

# Hidden condition: if i is richer than j then j is not richer than i (non-simmetry)
solver.add_assertion(ForAll([i,j], Implies((Function(richer, [i,j])),(Not(Function(richer, [j,i]))))))

# Charles hates no one that Agatha hates. 
solver.add_assertion(ForAll([i], Implies(Function(hates, [agatha,i]), Not(Function(hates, [charles,i])))))

# Agatha hates everybody except the butler.
solver.add_assertion(ForAll([i], Implies(NotEquals(i, butler), Function(hates, [agatha,i]))))

solver.add_assertion(Function(hates, [agatha,charles]))
solver.add_assertion(Function(hates, [agatha,agatha]))
solver.add_assertion(Not(Function(hates, [agatha,butler])))

# The butler hates everyone not richer than Aunt Agatha. 
solver.add_assertion(ForAll([i], Implies(Not(Function(richer, [i,agatha])), Function(hates, [butler,i]))))

# The butler hates everyone whom Agatha hates. 
solver.add_assertion(ForAll([i], Implies(Function(hates, [agatha,i]), Function(hates, [butler,i]) )))

# Noone hates everyone. 
solver.add_assertion(ForAll([i], Plus([Ite(Function(hates, [i,Int(j)]),Int(1),Int(0)) for j in range(n)]) <= Int(2)))

# Who killed Agatha? 
num_solutions = 0

print(solver.assertions)

while solver.solve():
    num_solutions += 1
    sat_model = {el[0].symbol_name():el[1] for el in solver.get_model()}
    print(sat_model)
    solver.add_assertion(Not(Equals(killer, sat_model['killer'])))
        
print("num_solutions:", num_solutions)