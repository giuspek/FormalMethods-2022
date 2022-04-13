from pysmt.shortcuts import *

RAM_servers = [2, 4, 4, 16, 8, 16, 16, 32, 8, 16, 8]
storage_servers = [100, 800, 1000, 8000, 3000, 6000, 4000, 2000, 1000, 10000, 1000]

RAM_vm = [1, 16, 4, 2, 4, 8, 2, 4, 16, 16, 12]
storage_vm = [100, 900, 710, 800, 7000, 4000, 800, 2500, 450, 3700, 1300]

solver = Solver()

srv_to_vm = []
use_server = []
n_servers = Symbol("n_servers", INT)

# Variables: pseudo-Boolean vars mapping pairs server-to-vm (1 if we store a vm to a server, 0 otherwise)
for s in range(len(RAM_servers)):
	srv_list = []
	for v in range(len(RAM_vm)):
		x = Symbol("srv{}_vm{}".format(s,v), INT)
		srv_list.append(x)
		solver.add_assertion(And(GE(x, Int(0)), LE(x, Int(1))))
	srv_to_vm.append(srv_list)

# Variables: use_server to check if a server has been used at least once. Pseudo-Boolean also in this case.
for s in range(len(RAM_servers)):
	x = Symbol("use_server{}".format(s), INT)
	use_server.append(x)
	solver.add_assertion(And(GE(x, Int(0)), LE(x, Int(1))))

# A virtual machine can be placed only on one server
for v in range(len(RAM_vm)):
	tmp = []
	for s in range(len(RAM_servers)):
		tmp.append(srv_to_vm[s][v])
	solver.add_assertion(Equals(Plus(tmp), Int(1)))

# Create linear relation that sum, for each server, the amount of RAM and storage used according to the virtual machines associated to it. 
# Notice how using Pseudo-Boolean operators drastically help us!

for s in range(len(RAM_servers)):
	tmp = []
	for v in range(len(RAM_vm)):
		tmp.append(Times(srv_to_vm[s][v], Int(RAM_vm[v])))
	solver.add_assertion(LE(Plus(tmp), Int(RAM_servers[s])))

	tmp = []
	for v in range(len(RAM_vm)):
		tmp.append(Times(srv_to_vm[s][v], Int(storage_vm[v])))
	solver.add_assertion(LE(Plus(tmp), Int(storage_servers[s])))

# If at least one virtual machine has been assigned to a server, then an additional pseudoboolean variable (use_srv) becomes one, meaning
# it has been used and must be counted.

for s in range(len(RAM_servers)):
	tmp = []
	for v in range(len(RAM_vm)):
		tmp.append(Equals(srv_to_vm[s][v], Int(1)))
	solver.add_assertion(Implies(Or(tmp), Equals(use_server[s], Int(1))))
	solver.add_assertion(Implies(Not(Or(tmp)), Equals(use_server[s], Int(0))))

# Sum all the use_srv pseudoBoolean variable into n_server

tmp = []
for s in range(len(RAM_servers)):
	tmp.append(use_server[s])
solver.add_assertion(Equals(Plus(tmp), n_servers))

write_smtlib(And(solver.assertions), "servers.smt2")