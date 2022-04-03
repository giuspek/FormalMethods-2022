from pysmt.shortcuts import *

# Support variables for readibility
n = 3
agatha = Int(0)
butler = Int(1)
charles = Int(2)

victim = agatha

solver = Solver()

who = ["agatha","butler","charles"]

killer = Symbol("killer", INT)

fu = FunctionType(BOOL, [INT, INT])

hates = Symbol("hates", fu)
richer = Symbol("richer", fu)

# Agatha, the butler, and Charles live in Dreadsbury Mansion, and 
# are the only ones to live there. 
solver.add_assertion(And(GE(killer,agatha), LE(killer,charles)))

# A killer always hates, and is no richer than his victim. 
solver.add_assertion(Function(hates, [killer,victim]))
solver.add_assertion(Not(Function(richer, [killer,victim])))


# Hidden condition: no one is richer than him-/herself (non-reflexivity)
for i in range(n):
    solver.add_assertion(Not(Function(richer, [Int(i),Int(i)])))

# Hidden condition: if i is richer than j then j is not richer than i (non-simmetry)
for i in range(n):
    for j in range(n):
        if i != j:
            solver.add_assertion(Iff((Function(richer, [Int(i),Int(j)])),(Not(Function(richer, [Int(j),Int(i)])))))

# Charles hates no one that Agatha hates. 
for i in range(n):
    solver.add_assertion(Implies(Function(hates, [agatha,Int(i)]), Not(Function(hates, [charles,Int(i)]))))


# Agatha hates everybody except the butler.
solver.add_assertion(Function(hates, [agatha,charles]))
solver.add_assertion(Function(hates, [agatha,agatha]))
solver.add_assertion(Not(Function(hates, [agatha,butler])))

# The butler hates everyone not richer than Aunt Agatha. 
for i in range(n):
    solver.add_assertion(Implies(Not(Function(richer, [Int(i),agatha])), Function(hates, [butler,Int(i)])))

# The butler hates everyone whom Agatha hates. 
for i in range(n):
    solver.add_assertion(Implies(Function(hates, [agatha,Int(i)]), Function(hates, [butler,Int(i)]) ))

# No one hates everyone. 
for i in range(n):
    solver.add_assertion(Plus([Ite(Function(hates, [Int(i),Int(j)]),Int(1),Int(0)) for j in range(n)]) < Int(3))

# Who killed Agatha? 
num_solutions = 0

while solver.solve():
    num_solutions += 1
    sat_model = {el[0].symbol_name():el[1] for el in solver.get_model()}
    print(sat_model)
    solver.add_assertion(Not(Equals(killer, sat_model['killer'])))
        
print("num_solutions:", num_solutions)