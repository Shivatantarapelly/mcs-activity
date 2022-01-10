# To sort (ascending and descending) a dictionary by value

dic = {'red': 2, 'green': 4, 'yellow': 3, 'black': 5, 'white': 1}
dsc = {}
asc = {}
li1 = []
for i, j in dic.items():
    li1.append(j)
for i in range(len(li1) - 1):
    for k in range(len(li1) - 1):
        if li1[k] < li1[k + 1]:
            li1[k], li1[k + 1] = li1[k + 1], li1[k]

# to sort descending order

for n in li1:
    for l, m in dic.items():
        if n == m:
            dsc[l] = m
            break
print(dsc)

# to sort ascending order

for n in range(len(li1) - 1, -1, -1):
    for l, m in dic.items():
        if li1[n] == m:
            asc[l] = m
            break

print(asc)

# --- sort dictionary by key ------

dic = {22: 'apple', 46: 'green', 38: 'yellow', 33: 'black', 29: 'white'}
l = []
for i in dic.keys():
    l.append(i)

for i in range(len(l) - 1):
    for k in range(len(l) - 1):
        if l[k] > l[k + 1]:
            l[k], l[k + 1] = l[k + 1], l[k]
print('keys after sorted: ', end=" ")
for j in l:
    print(j, end=" ")


# ------------- or -----------
print("")
dic = {22: 'apple', 46: 'green', 38: 'yellow', 33: 'black', 29: 'white'}
l = []
for i in dic.keys():
    l.append(i)
l2 = sorted(l)
print('keys after sorted: ', end=" ")
for j in l2:
    print(j, end=" ")
