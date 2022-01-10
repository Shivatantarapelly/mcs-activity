# Map two lists into a dictionary

l1 = [1, 2, 3]
l2 = ['shiva', 'sai', 'prasad']
dic = {}
if len(l1) == len(l2):
    for i in range(len(l1)):
        dic[l1[i]] = l2[i]
    print('created dictionary: ', dic)
else:
    print('length of both list must be same')
