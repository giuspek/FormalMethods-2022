from pysmt.shortcuts import *
from pysmt.solvers.msat import MathSAT5Solver

agatha = Int(1)
butler = Int(2)
charles = Int(3)
victim = agatha
killer = Symbol("killer", INT)

hates = Symbol("hates", FunctionType(BOOL, [INT, INT]))
richer = Symbol("richer", FunctionType(BOOL, [INT, INT]))

with Solver() as solver:
    solver: MathSAT5Solver

    # Someone who lives in Dreadbury Mansion killed Aunt Agatha.
    solver.add_assertion(ExactlyOne(Equals(killer, agatha), Equals(killer, butler), Equals(killer, charles)))

    # A killer always hates, and is never richer than his victim.
    solver.add_assertion(Function(hates, [killer, victim]))
    solver.add_assertion(Not(Function(richer, [killer, victim])))

    # Hidden condition: no one is richer than himself/herself (non-reflexivity)
    for person in [agatha, butler, charles]:
        solver.add_assertion(Not(richer(person, person)))

    # Hidden condition: if i is richer than j, then j is not richer than i (non-symmetry)
    for i in [agatha, butler, charles]:
        for j in [agatha, butler, charles, killer]:
            if i is not j:
                Iff(richer(i, j), Not(richer(j, i)))

    # Charles hates no one that Agatha hates.
    for person in [agatha, butler, charles]:
        solver.add_assertion(Implies(hates(agatha, person), Not(hates(charles, person))))

    # Agatha hates everybody except the butler.
    solver.add_assertion(hates(agatha, agatha))
    solver.add_assertion(hates(agatha, charles))
    solver.add_assertion(Not(hates(agatha, butler)))

    # The butler hates everyone not richer than Aunt Agatha.
    for person in [agatha, butler, charles]:
        solver.add_assertion(Implies(Not(Function(richer, [person, agatha])), Function(hates, [butler, person])))

    # The butler hates everyone whom Agatha hates.
    for person in [agatha, butler, charles]:
        solver.add_assertion(Implies(Function(hates, [agatha, person]), Function(hates, [butler, person])))

    # No one hates everyone.
    for i in [agatha, butler, charles]:
        solver.add_assertion(Not(And(Function(hates, [i, j]) for j in [agatha, butler, charles, killer])))

    n_solutions = 0
    while solver.solve():
        n_solutions += 1

        killer_value = solver.get_value(killer)
        if killer_value is agatha:
            print(f"Solution {n_solutions}: Agatha killed herself")
            solver.add_assertion(Not(Equals(killer, agatha)))
        elif killer_value is butler:
            print(f"Solution {n_solutions}: Butler killed Agatha")
            solver.add_assertion(Not(Equals(killer, butler)))
        elif killer_value is charles:
            print(f"Solution {n_solutions}: Charles killed Agatha")
            solver.add_assertion(Not(Equals(killer, charles)))
