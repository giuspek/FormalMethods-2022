from pysmt.shortcuts import *

day_company = {"dc{}{}".format(i,j): Symbol("dc{}{}".format(i,j), BOOL) for i in range(0,4) for j in "alsi"}
day_role = {"dr{}{}".format(i,j): Symbol("dr{}{}".format(i,j), BOOL) for i in range(0,4) for j in "cgrm"}

var = {**day_company, **day_role}

final_answer = ["20th: ", "21st: ", "22nd: ", "23rd: "]

msat = Solver()

# The Alpha Plus interview is 2 days before the meeting for the copywriter position.
msat.add_assertion(Or(And(var["dc0a"], var["dr2c"]), And(var["dc1a"], var["dr3c"])))

#The meeting for the graphic design position is some time after the Sancode interview
msat.add_assertion(And(Not(var["dr0g"]), Not(var["dc3s"]), Not(And(var["dr1g"], var["dc2s"])) )) 

# Of the interview for the sales rep position and the Laneplex interview, one is on August 23rd and the other is on August 20th.
msat.add_assertion(Or(And(var["dc0l"],var["dr3r"]), And(var["dc3l"],var["dr0r"])))

# The Streeter Inc. interview is 2 days after the Alpha Plus interview.
msat.add_assertion(Or(And(var["dc2i"], var["dc0a"]), And(var["dc3i"], var["dc1a"])))

# On the 23rd there is no interview for social media roles
msat.add_assertion(Not(var["dr3m"]))

# Each day must be associated to exactly one company
for i in range(0,4):
	msat.add_assertion(ExactlyOne([var["dc{}{}".format(i, j)] for j in "alsi"]))

# Each day must be associated to exactly one role
for i in range(0,4):
	msat.add_assertion(ExactlyOne([var["dr{}{}".format(i, j)] for j in "cgrm"]))	

# Each company must be associated to exactly one day
for j in "alsi":
	msat.add_assertion(ExactlyOne([var["dc{}{}".format(i, j)] for i in range(0,4)]))

# Each role must be associated to exactly one day
for j in "cgrm":
	msat.add_assertion(ExactlyOne([var["dr{}{}".format(i, j)] for i in range(0,4)]))


# Optional (but strongly suggested): prettify the results
companies = {"a": "Alpha Plus", "l":"Laneplex", "s": "Sancode", "i": "Streeter Inc."}
roles = {"c": "copywriter", 'g':'graphic design', 'r':'sales rep', 'm': 'social media'}

res = msat.solve()
if res:
	sat_model = {el[0].symbol_name():el[1] for el in msat.get_model()}
	for i in range(0,4):
		for j in "alsi":
			if sat_model["dc{}{}".format(i,j)] == Bool(True):
				final_answer[i] = final_answer[i] + companies[j] + " - "
		for j in "cgrm":
			if sat_model["dr{}{}".format(i,j)] == Bool(True):
				final_answer[i] = final_answer[i] + roles[j]
	print("\n".join(final_answer))
else:
	print("UNSAT")

# OPTIONAL: is the solution unique?
msat.add_assertion(Not(And(var["dc0a"], var["dc1s"], var["dc2i"], var["dc3l"], var["dr0r"], var["dr1m"], var["dr2c"], var["dr3g"])))

final_answer = ["20th: ", "21st: ", "22nd: ", "23rd: "]

res = msat.solve()
if res:
	sat_model = {el[0].symbol_name():el[1] for el in msat.get_model()}
	for i in range(0,4):
		for j in "alsi":
			if sat_model["dc{}{}".format(i,j)] == Bool(True):
				final_answer[i] = final_answer[i] + companies[j] + " - "
		for j in "cgrm":
			if sat_model["dr{}{}".format(i,j)] == Bool(True):
				final_answer[i] = final_answer[i] + roles[j]
	print("\n".join(final_answer))
else:
	print("UNSAT")

