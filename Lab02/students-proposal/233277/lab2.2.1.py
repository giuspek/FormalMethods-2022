from pysmt.shortcuts import *

days = ["20", "21", "22", "23"]
pos = ["cw", "gd", "sr", "sm"]
com = ["ap", "lp", "sc", "si"]

day_pos = {d + p: Symbol(d + p, BOOL) for d in days for p in pos}
day_com = {d + c: Symbol(d + c, BOOL) for d in days for c in com}
vars = {**day_pos, **day_com}

s = Solver()

# The Alpha Plus interview is 2 days before the meeting for the copywriter position
s.add_assertion(Or(And(vars["20ap"], vars["22cw"]), And(vars["21ap"], vars["23cw"])))

# The meeting for the graphic design position is sometime after the Sancode interview.
s.add_assertion(Not(vars["20gd"]))
s.add_assertion(Not(vars["23sc"]))
s.add_assertion(Not(And(vars["21gd"], vars["22sc"])))

# Of the interview for the sales rep position and the Laneplex interview, one is on August 23rd and the other is on August 20th.
s.add_assertion(Or(And(vars["23sr"], vars["20lp"]), And(vars["23lp"], vars["20sr"])))

# The Streeter Inc. interview is 2 days after the Alpha Plus interview.
s.add_assertion(Or(And(vars["20ap"], vars["22si"]), And(vars["21ap"], vars["23si"])))

# On the 23rd there is no interview for social media roles
s.add_assertion(Not(vars["23sm"]))

# 1 day exactly 1 job
for d in days:
    s.add_assertion(ExactlyOne(vars[f"{d}{p}"] for p in pos))

# 1 day exactly 1 company
for d in days:
    s.add_assertion(ExactlyOne(vars[f"{d}{c}"] for c in com))

# Not 2 days same job
for p in pos:
    s.add_assertion(ExactlyOne(vars[f"{d}{p}"] for d in days))

# Not 2 days same company
for c in com:
    s.add_assertion(ExactlyOne(vars[f"{d}{c}"] for d in days))

result = s.solve()

if result:
    print("SAT")
    answer = {"20": {}, "21": {}, "22": {}, "23": {}}
    for var in vars:
        if str(s.get_value(vars[var])) == 'True':
            date = var[:2]
            val = var[2:]
            if val in pos:
                answer[date]["pos"] = val
            elif val in com:
                answer[date]["com"] = val
    pos_dict = {"cw": "Copywriter", "gd": "Graphic Design", "sr": "Sales Rep", "sm": "Social Media"}
    com_dict = {"ap": "Alpha Plus", "lp": "Laneplex", "sc": "Sancode", "si": "Streeter Inc."}
    for a in answer:
        print("Date: {}\n- Position: {}\n- Company: {}".format(a, pos_dict[answer[a]["pos"]], com_dict[answer[a]["com"]]))
else:
    print("UNSAT")


