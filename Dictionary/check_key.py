# Check if a given key already exists in a dictionary.

x = int(input('enter how many item you want to add to dictionary: '))
dic = {}
for i in range(x):
    key = input('enter the key: ')
    value = input('enter the value: ')
    dic[key] = value

print(dic)
y = input('enter the key to find whether it exist id dic or not: ')
for i, j in dic.items():
    if y == i:
        n = True
        break
    else:
        n = False

if n is True:
    print('key exists')
else:
    print('key doesnt exists')
