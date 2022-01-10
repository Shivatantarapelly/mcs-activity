# Generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)

n = int(input('enter a number to generate dictionary: '))
dic = {}
for i in range(1, n + 1):
    dic[i] = i * i

print(dic)

# Print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys

n = 15
dic = {}
for i in range(1, n + 1):
    dic[i] = i * i

print(dic)
