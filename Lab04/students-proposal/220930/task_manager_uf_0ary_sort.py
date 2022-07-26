"""
From task_manager.py:
Model 1: D E A C B
Model 2: D A E C B
Model 3: D A C E B
"""

from pysmt.shortcuts import *
from pysmt.solvers.z3 import Z3Solver

my_sort = Type("my_sort", arity=0)
after = Symbol("after", FunctionType(BOOL, [my_sort, my_sort]))

a = Symbol("A", my_sort)
b = Symbol("B", my_sort)
c = Symbol("C", my_sort)
d = Symbol("D", my_sort)
e = Symbol("E", my_sort)

with Solver(name="z3") as z3:
    z3: Z3Solver

    i, j, k = Symbol("i", my_sort), Symbol("j", my_sort), Symbol("k", my_sort)

    # Non-symmetry
    # ∀i,j, i≠j => after(i,j) => !after(j,i)
    z3.add_assertion(ForAll([i, j], Implies(NotEquals(i, j), Implies(after(i, j), Not(after(j, i))))))

    # Non-reflexivity
    # ∀i, !after(i,i)
    z3.add_assertion(ForAll([i], Not(after(i, i))))

    # Transitivity
    # ∀i,j, i≠j≠k ∧ after(i,j) ∧ after(j,k) => after(i,k)
    z3.add_assertion(ForAll([i, j, k], Implies(AllDifferent(i, j, k) & after(i, j) & after(j, k), after(i, k))))

    z3.add_assertion(AllDifferent(a, b, c, d, e))

    # We can execute A after D is completed.
    z3.add_assertion(after(a, d))

    # We can execute B after C and E are completed.
    z3.add_assertion(after(b, c) & after(b, e))

    # We can execute E after B or D are completed.
    z3.add_assertion(after(e, b) | after(e, d))

    # We can execute C after A is completed.
    z3.add_assertion(after(c, a))

    # write_smtlib(And(z3.assertions), "task_manager.smt2")  # UFLIRA

    z3.solve()  # The solver will infer all the relationships between the tasks

    model = [after(task1, task2)
             for task1 in [a, b, c, d, e] for task2 in [a, b, c, d, e]
             if z3.get_value(after(task1, task2)) == TRUE()]
    print(model)
    # [after(A, D), after(B, A), after(B, C), after(B, D), after(B, E), after(C, A), after(C, D), after(E, D)]

    # print(z3.get_model())
    # The solver can assign the variables as it pleases, therefore the following values are "meaningless"
    # and do not suggest an actual task ordering.
    # A := 2
    # D := 1
    # B := 4
    # C := 3
    # E := 0
