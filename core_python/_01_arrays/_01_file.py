""""
Array: an array is an object that stores a group of elements (or values) of same datatype.
the main advantage of an array is to store and process a group of elements easily.
there are two points to be remembered in case of arrays in python:
1) arrays can store only one type of data.
2) arrays can increase or decrease their size dynamically. it means we need not to declare the size of the array.

in python, we can work with arrays by importing the standard module by the name "arrays"

Advantages:
-----------
* arrays are similar to list. the main difference is that array can store only one type of elements.
  when dealing with huge number of elements arrays will use less memory than lists and offer faster
  execution than list.
* the size of an array is not fixed in python. hence we need not specify the size of array to store
  elements in the beginning.
* array can grow or shrink in memory dynamically.(during runtime)
* arrays are useful to handle a collection of elements like a group of numbers or chars
* methods that are useful to process an array are available in 'array' module.

"""
import array

# creating an array

arr = array.array('i', [5, 6, -7, 8])
print('elements of array: ', end=' ')
for i in arr:
    print(i, end=' ')
print('')
print('========================================')

arr = array.array('u', ['a', 'b', 'c', 'd'])
print('elements of array: ', end=' ')
for i in arr:
    print(i, end=' ')
print('')
print('========================================')

# creating an array from another array

arr1 = array.array('i', [1, 2, 3, 4])
arr2 = array.array(arr1.typecode, (a ** 2 for a in arr1))
print('the elements of arr2: ', end=' ')
for i in arr2:
    print(i, end=' ')
print('')
print('========================================')

# slicing and indexing using arrays

arr1 = array.array('i', [10, 20, 30, 40])
print('length of the array:', len(arr1))
print('1st index element:', arr1[0])
print('3rd index element:', arr1[2])
print('1st two elements in array using slicing:', arr1[0:2])
print('alternative elements in array using slicing:', arr1[::2])

print('========================================')

"""
methods                                  Description
--------                                 ------------
append(x)         |  adds an element x at the end of existing array
count(x)          |  returns the no. of occurrence  of x in the array 
extend(x)         |  appends x at the end of the array. x can be another array or iterable object
fromfile(f,n)     |  reads n items from the file object f and append to end of array.
fromlist(lst)     |  appends items from the lst to end of the array.
fromstring(s)     |  appends items from string s to end of array.
index(x)          |  returns the position number of the first occurrence of x in array.
insert(x)         |  insert x in the position i in array
pop(x)            |  removes the item x from array and returns it
pop()             |  removes the last item from array
remove(x)         |  removes the first occurrence of x in array. raises value error if not found
reverse()         |  reverse the order of elements in the array
tofile(f)         |  writes all elements to the file f.
tolist()          |  converts the array into list
tostring()        |  convert the array into a string

variable             Description
--------             -----------
typecode    |   represent the type code character used to create the array
itemsize    |   represent the size of items stored in the array 

"""

# operation on arrays

arr = array.array('i', [10, 20, 30, 40, 50, 60])
arr.append(70)
print('appending 70 into an array: ', arr)
print('========================================')

arr.insert(1, 100)
print('inserting 100 at 1st index position: ', arr)
print('========================================')

arr.remove(20)
print('array after removing 20: ', arr)
print('========================================')

arr.pop()
print('deleting last element from array: ', arr)
print('========================================')

x = arr.index(100)
print('first occurrence position of element 100 in array: ', x)
print('========================================')

lst = arr.tolist()
print('before converting to list array is: ', arr)
print('after converting array to list: ', lst)

"""
Types of arrays:
* single dimensional arrays
  these arrays represents only one row or one column of element.
  ex: arr = array('i',[10,20,30]
* multi dimensional arrays
  these arrays represents more than one row and more than one column of elements.
  ex: arr = array([[11,12,13,14],
                   [21,22,23,24],
                   [31,32,33,34]]

# working with arrays using numpy:
* numpy is a package which used to deal with scientific calculation in python.
  numpy is useful to create and also process single and multidimensional arrays.

# creating an array in numpy can be done in several ways
  using functions like array(), linespace(), logspace(), arange(), zeros(), ones()

"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print('array using numpy: ', arr)
print('========================================')

arr = np.linspace(1, 10, 5)
print('array using line space: ', arr)
print('========================================')

arr = np.logspace(2, 6, 5)
print('array using logspace: ', arr)
print('========================================')

arr = np.arange(5, 20, 5)
print('array using arrange: ', arr)
print('========================================')

arr = np.zeros(5, int)
print('array using zeros: ', arr)
print('========================================')

arr = np.ones(5, float)
print('array using ones: ', arr)
print('========================================')

# reshape()
arr1 = np.arange(9)
print('array before reshaping: ', arr1)
arr1 = arr1.reshape(3, 3)
print('using reshape converting 1dim array to 3 dim array:\n', arr1)
print('========================================')

# flatten()

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print('array before flatten:\n ', arr1)
arr1 = arr1.flatten()
print('flattening the 2 dim array to single dim: ', arr1)
print('========================================')

# ones, zeros for multi dimensional

arr = np.ones((3, 4), float)
arr1 = np.zeros((4, 3), int)
print('creating an 3*4 arrays using ones():\n ', arr)
print('creating an 4*3 arrays using zeros():\n ', arr1)
print('========================================')

# eye(), reshape()

arr = np.eye(3)
print('creating an 3dim array using eye():\n ', arr)

arr1 = np.array([11, 52, 63, 78, 69, 42, 63, 36])
arr1 = np.reshape(arr1, (2, 4))
print('converting the 1dim array to 2*4 using \n', arr1)
print('========================================')

# indexing

arr = np.array([11, 52, 63, 78, 69, 42, 63, 36, 45, 65, 26, 7, 89, 46, 25, 86])
arr = np.reshape(arr, (4, 4))
print('created 4*4 array is: \n', arr)
print('getting the value 7 from above array using indexing: ', arr[2][3])
print('getting the value 42 from above array using indexing: ', arr[1][1])
print('========================================')

# slicing

print('getting the value 63,36,26,7 from above array using slicing:\n ', arr[1:3, 2: ])
print('getting the value 11,52,69,42,45,65 from above array using slicing:\n ', arr[0:3, 0:2])
print('getting the value 69 from above array using slicing:\n ', arr[1:2, 0:1])

# diagonal

arr = np.array([11, 52, 63, 78, 69, 42, 63, 36, 45, 65, 26, 7, 89, 46, 25, 86])
arr = np.reshape(arr, (4, 4))
d = np.diagonal(arr)
print('print the diagonal elements of 4*4 array: ', d)
print('print the biggest number in array: ', arr.max())
print('print the smallest number in array: ', arr.min())
print('print the sum of all number in array: ', arr.sum())

#  creating a matrix

m = np.matrix(np.arange(9).reshape(3, 3))
print('creating 3*3 matrix: \n', m)

# array with random numbers

arr = np.random.rand(2, 3)
print('creating 2*3 matrix using random numbers: \n', arr)












