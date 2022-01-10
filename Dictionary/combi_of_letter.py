# Create and display all combinations of letters, selecting each letter from a different key in a dictionary

dic = {1: ['apple', 'banana'], 2: ['pineapple', 'mango']}
print('no.of combinations:')
for x in dic[1]:
    for y in dic[2]:
        print(x, ' ', y)

# Find the highest 3 values in a dictionary.

dic = {'a': 50, 'b': 63, 'c': 45, 'd': 85, 'f': 66}
dic1 = {}
li = []
li1 = []
for i in dic.values():
    li.append(i)

for l in range(len(li) - 1):
    for m in range(len(li) - 1):
        if li[m] > li[m + 1]:
            li[m], li[m + 1] = li[m + 1], li[m]
for i in range(len(li) - 1, -1, -1):
    li1.append(li[i])
    if i == len(li) - 3:
        break

for k in li1:
    for i, j in dic.items():
        if j == k:
            dic1[i] = k
print(dic1)
