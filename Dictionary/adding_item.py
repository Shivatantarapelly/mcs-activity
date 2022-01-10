# adding an items to dictionary

x = int(input('enter how many item you want to add to dictionary: '))
dic = {}
for i in range(x):
    key = input('enter the key: ')
    value = input('enter the value: ')
    dic[key] = value

print(dic)

