from pysmt.shortcuts import *

NUM_SV = 11
NUM_VM = 11

ram_sv = [2, 4, 4, 16, 8, 16, 16, 32, 8, 16, 8]
sto_sv = [100, 800, 1000, 8000, 3000, 6000, 4000, 2000, 1000, 10000, 1000]

ram_vm = [1, 16, 4, 2, 4, 8, 2, 4, 16, 16, 12]
sto_vm = [100, 900, 710, 800, 7000, 4000, 800, 2500, 450, 3700, 1300]

sv_vm = {"sv{}vm{}".format(i, j): Symbol("sv{}vm{}".format(i, j), INT) for i in range(NUM_SV) for j in range(NUM_VM)}
sv_used = {"sv{}_used".format(i): Symbol("sv{}_used".format(i), INT) for i in range(NUM_SV)}

vars = {**sv_vm, **sv_used}

s = Solver()

# Define range of sv_vm and sv_used to be in (0,1)
for i in range(NUM_SV):
    s.add_assertion(And(LE(vars["sv{}_used".format(i)], Int(1)), GE(vars["sv{}_used".format(i)], Int(0))))
    for j in range(NUM_VM):
        s.add_assertion(And(LE(vars["sv{}vm{}".format(i, j)], Int(1)), GE(vars["sv{}vm{}".format(i, j)], Int(0))))

# Each vm 1 server only
for j in range(NUM_VM):
    s.add_assertion(ExactlyOne(Equals(vars["sv{}vm{}".format(i, j)], Int(1)) for i in range(NUM_SV)))

# If a server is used by 1 VM => It is used
for i in range(NUM_SV):
    s.add_assertion(Implies(Or(Equals(vars["sv{}vm{}".format(i, j)], Int(1)) for j in range(NUM_VM)), Equals(vars["sv{}_used".format(i)], Int(1))))

# Constraint about RAM and storage of servers and VMs
for i in range(NUM_SV):
    # RAM
    s.add_assertion(LE(Plus(Times(vars["sv{}vm{}".format(i, j)], Int(ram_vm[j])) for j in range(NUM_VM)), Int(ram_sv[i])))
    # Storage
    s.add_assertion(LE(Plus(Times(vars["sv{}vm{}".format(i, j)], Int(sto_vm[j])) for j in range(NUM_VM)), Int(sto_sv[i])))

# Get number of server used
vars["num_sv_used"] = Symbol("num_sv_used", INT)
s.add_assertion(Equals(vars["num_sv_used"], Plus(vars["sv{}_used".format(i)] for i in range(NUM_SV))))

formula = And(s.assertions)
write_smtlib(formula, "lab6.6.3.smt2")

if s.solve():
    print("SAT")
    for var in vars:
        print("{}: {}".format(var, s.get_value(vars[var])))
else:
    print("UNSAT")
