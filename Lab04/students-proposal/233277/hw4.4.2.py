from pysmt.shortcuts import *

# Tasks represented in their order
vars = {"{}".format(char): Symbol("{}".format(char), INT) for char in "abcde"}

s = Solver()

# Tasks must be ordered in [1,2,3,4,5]
for char in "abcde":
    s.add_assertion(And(GE(vars["{}".format(char)], Int(1)), LE(vars["{}".format(char)], Int(5))))

# We can execute A after D is completed
s.add_assertion(GT(vars["a"], vars["d"]))

# We can execute B after C and E are completed
s.add_assertion(And(GT(vars["b"], vars["c"]), GT(vars["b"], vars["e"])))

# We can execute E after B or D are completed
s.add_assertion(Or(GT(vars["e"], vars["b"]), GT(vars["e"], vars["d"])))

# We can execute C after A is completed
s.add_assertion(GT(vars["c"], vars["a"]))

# All tasks must be done in different orders
s.add_assertion(AllDifferent(vars["{}".format(char)] for char in "abcde"))

if s.solve():
    print("SAT")
    order = [int(str(s.get_value(vars[var]))) for var in vars]
    temp = list(zip(["A", "B", "C", "D", "E"], order))
    ordered_tasks = [task for task, _ in sorted(temp, key=lambda x: x[1])]
    for task in ordered_tasks[:-1]:
        print(task, end=" -> ")
    print(ordered_tasks[-1])
    print("The task that will execute for last is {}".format(ordered_tasks[-1]))
else:
    print("UNSAT")