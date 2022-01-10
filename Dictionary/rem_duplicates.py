# Remove duplicates values from Dictionary

dic = {'apple': 10, 'mango': 20, 'banana': 30, 'grapes': 30, 'pineapple': 20}
l1 = []
dic1 = {}
for i, j in dic.items():
    if j not in l1:
        l1.append(j)
        dic1[i] = j
    else:
        pass
print(dic1)

# Combine two dictionary adding values for common keys.

dic = {'apple': 10, 'mango': 20, 'banana': 30}
dic1 = {'grapes': 30, 'apple': 30, 'banana': 50, 'pineapple': 20}
for k, j in dic.items():
    if k in dic1:
        dic1[k] += j
for l, m in dic.items():
    if l not in dic1.keys():
        dic1[l] = m

print(dic1)

# Print all unique values in a dictionary.

dic = {'grapes': 30, 'apple': 40, 'banana': 80, 'pineapple': 20, 'mango': 20, 'watermelon': 40}
l = []
for i in dic.values():
    if i not in l:
        l.append(i)
print('unique elements in dictionary: ', end=' ')
for j in l:
    print(j, end=' ')
