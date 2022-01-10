# Combine values in python list of dictionaries.


dic = {'name': ['shiva', 'sai'], 'tech': ['python', 'java', 'c']}
l = []

for i in dic['name']:
    for j in dic['tech']:
        dic1 = {}
        dic1['name'] = i
        dic1['tech'] = j
        l.append(dic1)
print(l)


# Create a dictionary from a string.

st = 'a-10,b-20,c-30,d-40'
nst = st.split(',')
l = []
dic = {}
for i in nst:
    s = i.split('-')
    l.extend(s)
i = 0
while i < len(l):
    dic[l[i]] = l[i+1]
    i += 2
print(dic)