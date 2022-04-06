'''
1. The student who will major in English is either Tracy or the student who received the $30,000 scholarship.
2. The four students are Iris, the person who received the $40,000 scholarship, the student who will major in Archaeology and the student who received the $35,000 scholarship.
3. Kerry was awarded $10,000 less than the student who will major in Mathematics.
4. Of the student who will major in English and the student who received the $40,000 scholarship, one is Erma and the other is Tracy.
'''

from pysmt.shortcuts import *

scholarship_person = {"sp{}{}".format(i,j): Symbol("sp{}{}".format(i,j), BOOL) for i in range(0,4) for j in "eikt"}
scholarship_major = {"sm{}{}".format(i,j): Symbol("sm{}{}".format(i,j), BOOL) for i in range(0,4) for j in "aemp"}

var = {**scholarship_person, **scholarship_major}

final_answer = ["$25000: ", "$30000: ", "$35000: ", "$40000: "]

msat = Solver()
# 1. The student who will major in English is either Tracy or the student who received the $30,000 scholarship.
tracy_english = Or([And(var[f"sp{i}t"], var[f"sm{i}e"]) for i in range(0,4)])
msat.add_assertion(
	And(
		Or(tracy_english, var["sm1e"]), 
		Not(var["sp1t"])
	)
)

# 2. The four students are Iris, the person who received the $40,000 scholarship, the student who will major in Archaeology and the student who received the $35,000 scholarship.
iris_arch = Or([And(var[f"sp{i}i"], var[f"sm{i}a"]) for i in range(0,4)])
temp = Or([Or(var[f"sp{i}i"], var[f"sm{i}a"]) for i in range(2,4)])
msat.add_assertion(
	Not(
		Or(
			temp,
			iris_arch
		)
	)
)

# 3. Kerry was awarded $10,000 less than the student who will major in Mathematics.
msat.add_assertion(
	Or(
		And(var["sp0k"], var["sm2m"]),
		And(var["sp1k"], var["sm3m"]),
	)
)
# 4. Of the student who will major in English and the student who received the $40,000 scholarship, one is Erma and the other is Tracy.
erma_english = Or([And(var[f"sp{i}e"], var[f"sm{i}e"]) for i in range(0,4)])
msat.add_assertion(
	Or(
		And(erma_english, var["sp3t"]),
		And(tracy_english, var["sp3e"])
	)
)

# Each scholarship must be associated to exactly one person
for i in range(0,4):
	msat.add_assertion(ExactlyOne([var["sp{}{}".format(i, j)] for j in "eikt"]))

# Each scholarship must be associated to exactly one major
for i in range(0,4):
	msat.add_assertion(ExactlyOne([var["sm{}{}".format(i, j)] for j in "aemp"]))	

# Each person must be associated to exactly one scholarship
for j in "eikt":
	msat.add_assertion(ExactlyOne([var["sp{}{}".format(i, j)] for i in range(0,4)]))

# Each major must be associated to exactly one scholarship
for j in "aemp":
	msat.add_assertion(ExactlyOne([var["sm{}{}".format(i, j)] for i in range(0,4)]))


# Optional (but strongly suggested): prettify the results
people = {"e": "Erma", "i":"Iris", "k": "Kerry", "t": "Tracy"}
majors = {"a": "Archaeology", 'e':'English', 'm':'Mathematics', 'p': 'Physics'}

res = msat.solve()
if res:
	sat_model = {el[0].symbol_name():el[1] for el in msat.get_model()}
	for i in range(0,4):
		for j in "eikt":
			if sat_model["sp{}{}".format(i,j)] == Bool(True):
				final_answer[i] = final_answer[i] + people[j] + " - "
		for j in "aemp":
			if sat_model["sm{}{}".format(i,j)] == Bool(True):
				final_answer[i] = final_answer[i] + majors[j]
	print("\n".join(final_answer))
else:
	print("UNSAT")

# OPTIONAL: is the solution unique?
msat.add_assertion(Not(And(var["sp0i"], var["sp1k"], var["sp2t"], var["sp3e"], var["sm0p"], var["sm1a"], var["sm2e"], var["sm3m"])))

final_answer = ["$25000: ", "$30000: ", "$35000: ", "$40000: "]

res = msat.solve()
if res:
	sat_model = {el[0].symbol_name():el[1] for el in msat.get_model()}
	for i in range(0,4):
		for j in "eikt":
			if sat_model["sp{}{}".format(i,j)] == Bool(True):
				final_answer[i] = final_answer[i] + people[j] + " - "
		for j in "aemp":
			if sat_model["sm{}{}".format(i,j)] == Bool(True):
				final_answer[i] = final_answer[i] + majors[j]
	print("\n".join(final_answer))
else:
	print("UNSAT")
