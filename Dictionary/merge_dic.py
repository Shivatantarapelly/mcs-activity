# Merge two Python dictionaries

dic1 = {'apple': 20, 'banana': 60, 'mango': 30}
dic2 = {'python': 20, 'java': 30}
dic3 = dic1.copy()
for i, j in dic2.items():
    dic3[i] = j

print('the updated dictionary: ', dic3)

# ------------ or ------------------

dic1 = {'apple': 20, 'banana': 60, 'mango': 30}
dic2 = {'python': 20, 'java': 30}
dic1.update(dic2)
print('the updated dictionary: ', dic1)

# ----- Sum all the items in a dictionary ------------

dic1 = {'apple': 20, 'banana': 60, 'mango': 30}
tot = 0
for j in dic1.values():
    tot += j
print('sum of items', tot)


# Multiply all the items in a dictionary

dic1 = {'apple': 2, 'banana': 6, 'mango': 3}
tot = 1
for j in dic1.values():
    tot *= j
print('multiply of items', tot)
