# Logic puzzle: 
# - Size: 3x5 grid 
# - Difficulty: Challenging

from pysmt.shortcuts import *

subj = ["co", "de", "no", "sc", "wa"] # Corsica, Denmark, North America, Scandinavia, Warsaw
cart = ["bl", "ca", "go", "je", "mu"] # Bleux, Caronelli, Gostaldo, Jenson, Muenster
year = ["13", "31", "49", "67", "85"] # 17th century

subjyear = {"{}{}".format(s, y): Symbol("{}{}".format(s, y), BOOL) for s in subj for y in year}
cartyear = {"{}{}".format(c, y): Symbol("{}{}".format(c, y), BOOL) for c in cart for y in year}
subjcart = {"{}{}".format(s, c): Symbol("{}{}".format(s, c), BOOL) for s in subj for c in cart}

vars = {**subjyear, ** cartyear, **subjcart}

s = Solver()

# Gostaldo's map is either the map of Warsaw or the print published in 1713
s.add_assertion(Or(vars["wago"], vars["go13"]))

# The map published in 1785 was of Scandinavia
s.add_assertion(vars["sc85"])

# The map published in 1767 wasn't of Corsica
s.add_assertion(Not(vars["co67"]))

# Of the print of North Africa and Caronelli's map, one was published in 1713 and the other was published in 1731
s.add_assertion(Or(And(vars["no13"], vars["ca31"]), And(vars["no31"], vars["ca13"])))

# Muenster's print, the map of Warsaw, the map of Denmark and the map published in 1731 are all different maps
s.add_assertion(Not(vars["wamu"]))
s.add_assertion(Not(vars["demu"]))
s.add_assertion(Not(vars["mu31"]))
s.add_assertion(Not(vars["wa31"]))
s.add_assertion(Not(vars["de31"]))

# Bleux's map was of Corsica
s.add_assertion(vars["cobl"])

# Each subject a different year
for sub in subj:
    s.add_assertion(ExactlyOne(vars["{}{}".format(sub, y)] for y in year))

# Each cartographer a different year
for c in cart:
    s.add_assertion(ExactlyOne(vars["{}{}".format(c, y)] for y in year))

# Each subject a cartographer
for sub in subj:
    s.add_assertion(ExactlyOne(vars["{}{}".format(sub, c)] for c in cart))

# Each year 1 subject
for y in year:
    s.add_assertion(ExactlyOne(vars["{}{}".format(sub, y)] for sub in subj))

# Each year 1 cartographer
for y in year:
    s.add_assertion(ExactlyOne(vars["{}{}".format(c, y)] for c in cart))

# Each cartographer 1 subject
for c in cart:
    s.add_assertion(ExactlyOne(vars["{}{}".format(sub, c)] for sub in subj))

# INCLUDING 3 IMPLICATIONS, JUST TO BE SURE
for c in cart:
    for sub in subj:
        for y in year:
            # 1 cartographer a year, 1 cartographer makes 1 subject -> The subject made in that year
            s.add_assertion(Implies(And(vars["{}{}".format(c, y)], vars["{}{}".format(sub, c)]), vars["{}{}".format(sub, y)]))
            # 1 cartographer a year, 1 subject a year -> The subject made by that cartographer
            s.add_assertion(Implies(And(vars["{}{}".format(c, y)], vars["{}{}".format(sub, y)]), vars["{}{}".format(sub, c)]))
            # 1 cartographer makes 1 subject, 1 subject a year -> The cartographer printed that year
            s.add_assertion(Implies(And(vars["{}{}".format(sub, c)], vars["{}{}".format(sub, y)]), vars["{}{}".format(c, y)]))

if s.solve():
    print("SAT")
    true_sy = {"{}".format(sub): 0 for sub in subj}
    true_cy = {"{}".format(c): 0 for c in cart}
    for var in vars:
        if str(s.get_value(vars[var]) )== 'True':
            if var[:2] in subj:
                if var[2:] in year:
                    true_sy[var[:2]] = int(var[2:])
            elif var[:2] in cart:
                true_cy[var[:2]] = int(var[2:])
    answer = {13: {}, 31: {}, 49: {}, 67: {}, 85: {}}
    for sy in true_sy:
        answer[true_sy[sy]]["subject"] = sy
    for cy in true_cy:
        answer[true_cy[cy]]["cartographer"] = cy
    subj_dict = {"co": "Corsica", "de": "Denmark", "no": "North America", "sc": "Scandinavia", "wa": "Warsaw"} # Corsica, Denmark, North America, Scandinavia, Warsaw
    cart_dict = {"bl": "Bleux", "ca": "Caronelli", "go": "Gostaldo", "je": "Jenson", "mu": "Muenster"} # Bleux, Caronelli, Gostaldo, Jenson, Muenster
    for ans in answer:
        print("Year: {}".format(1700 + ans))
        print("- Subject: {}".format(subj_dict[answer[ans]["subject"]]))
        print("- Cartographer: {}".format(cart_dict[answer[ans]["cartographer"]]))
else:
    print("UNSAT")    