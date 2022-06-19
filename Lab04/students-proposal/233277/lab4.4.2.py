from pysmt.shortcuts import *

people = ["a", "b", "c"] # Agatha, Butler, Charles
people_dict = {"a": "Agatha", "b": "Butler", "c": "Charles"}

is_killer = {"{}".format(char): Symbol("{}".format(char), BOOL) for char in people}
hate = {"{}h{}".format(c1, c2): Symbol("{}h{}".format(c1, c2), BOOL) for c1 in people for c2 in people}
richer = {"{}r{}".format(c1, c2): Symbol("{}r{}".format(c1, c2), BOOL) for c1 in people for c2 in people}

vars = {**is_killer, **hate, **richer}

s = Solver()

# A killer always hates victim and never richer than the victim
for char in people:
    s.add_assertion(Implies(vars["{}".format(char)], And(vars["{}ha".format(char)], Not(vars["{}ra".format(char)]))))

# Charles hates no one that Aunt Agatha hates
for char in people:
    s.add_assertion(Implies(vars["ah{}".format(char)], Not(vars["ch{}".format(char)])))

# Agatha hates everyone except the butler
s.add_assertion(And(vars["ah{}".format(char)] for char in people if char != "b"))
s.add_assertion(Not(vars["ahb"]))

# The butler hates everyone not richer than Aunt Agatha
for char in people:
    s.add_assertion(Implies(Not(vars["{}ra".format(char)]), vars["bh{}".format(char)]))

# The butler hates everyone Aunt Agatha hates
for char in people:
    s.add_assertion(Implies(vars["ah{}".format(char)], vars["bh{}".format(char)]))

# No one hates everyone
for c1 in people:
    s.add_assertion(Not(And(vars["{}h{}".format(c1, c2)] for c2 in people)))

# Exactly one of them kills Agatha
s.add_assertion(ExactlyOne(vars["{}".format(char)] for char in people))

# No one can be richer than him/herself
for char in people:
    s.add_assertion(Not(vars["{}r{}".format(char, char)]))

# If c1 richer than c2 then c2 not richer than c1
for c1 in people:
    for c2 in people:
        s.add_assertion(Implies(vars["{}r{}".format(c1, c2)], Not(vars["{}r{}".format(c2, c1)])))

if s.solve():
    print("SAT")
    for p in people:
        if str(s.get_value(vars[p])) == 'True':
            print("{} killed Agatha".format(people_dict[p]))
else:
    print("UNSAT")