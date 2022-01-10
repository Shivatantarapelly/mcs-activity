# Get the maximum and minimum value in a dictionary.

dic1 = {'maths': 80, 'science': 63, 'social': 68, 'english': 75, 'biology': 35}
l = []
for i in dic1.values():
    l.append(i)
for k in range(len(l) - 1):
    for j in range(len(l) - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
print('minimum value in dictionary:', l[0])
print('maximum value in dictionary:', l[-1])
