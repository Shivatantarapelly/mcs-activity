# program to sort array elements using bubble sort technique
from array import *

"""

arr = array('i', [])
n = int(input('how many elements you want to store: '))
for i in range(n):
    n1 = int(input('enter the numbers you want to store: '))
    arr.append(n1)
print('original array: ', arr)

x = False
for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
            x = True
    if x == False:
        break
    else:
        x = False

print('sorted array is: ', arr)
"""
# program to search for the position of an element in an array using sequential search

"""
arr = array('i', [])
n = int(input('how many elements you want to store: '))
for i in range(n):
    n1 = int(input('enter the numbers you want to store: '))
    arr.append(n1)
print('original array: ', arr)
s = int(input("enter element to search: "))
for i in range(len(arr)):
    if s == arr[i]:
        print("position of element you entered is: ", i+1)
        x = False
        break
    else:
        x= True
if x == True:
    print("no element found")
"""

# programs using numpy

import numpy as np

arr1 = np.array([1, 2, 3, 0])
arr2 = np.array([0, 2, 3, 1])

arr = arr1 > arr2
print("result of arr1>arr2", arr)   # o/p [true,false,false,false]
print('checking if any element is true:', any(arr))   # o/p true
print('checking if all element are true:', all(arr))   # o/p false

arr1 = np.array([11, 23, 35, 40])
arr2 = np.array([20, 22, 34, 41])
arr = np.where(arr1 > arr2, arr1, arr2)
print('comparing two arrays and retrieve the biggest elements: ', arr)


# creating a view of existing array

arr1 = np.arange(1, 10)
arr2 = arr1.view()
print('original array: ', arr1)
print('view of original array: ', arr2)
arr2[0] = 100           # will get change in both arrays
print('original array: ', arr1)
print('view of original array: ', arr2)


#  creating a copy of existing array

arr1 = np.arange(1, 10)
arr2 = arr1.copy()
print('original array: ', arr1)
print('copy of original array: ', arr2)
arr2[0] = 100           # will get change in only arr2
print('original array: ', arr1)
print('view of original array: ', arr2)












