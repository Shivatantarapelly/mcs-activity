"""
What is Python Generator?
generator function is a function which returns generator - iterator with the help of yield keyword.
here generator - iterator is a special type of iterator i.e generator function returns iterators.
all generator - iterators are iterator but all iterators are not generator - iterators.

There is a lot of complexity in creating iteration in Python;
we need to implement __iter__() and __next__() method to keep track of internal states.

It is a lengthy process to create iterators. That's why the generator plays an essential role in simplifying this
process. If there is no value found in iteration, it raises StopIteration exception.

How to Create Generator function in Python?

It is quite simple to create a generator in Python. It is similar to the normal function defined by the
def keyword and uses a yield keyword instead of return. Or we can say that if the body of any function contains a
yield statement, it automatically becomes a generator function. Consider the following example:
"""


def simple():
    for i in range(10):
        if i % 2 == 0:
            yield i

        # Successive Function call using for loop


for j in simple():
    print(j)

"""
yield vs. return
The yield statement is responsible for controlling the flow of the generator function. It pauses
the function execution by saving all states and yielded to the caller. Later it resumes execution when a successive
function is called. We can use the multiple yield statement in the generator function.

The return statement returns a value and terminates the whole function and only one return statement can be used in
the function.

Using multiple yield Statement

We can use the multiple yield statement in the generator function. Consider the following example.
"""
print("--------------------------------------------------------------------------------------------------")


def multiple_yield():
    str1 = "First String"
    yield str1

    str2 = "Second string"
    yield str2

    str3 = "Third String"
    yield str3


obj = multiple_yield()
print(next(obj))
print(next(obj))
print(next(obj))

"""
Difference between Generator function and Normal function:

Normal function contains only one return statement whereas generator function can contain one or more yield statement.
When the generator functions are called,the normal function is paused immediately and control transferred to the caller.
Local variable and their states are remembered between successive calls.
StopIteration exception is raised automatically when the function terminates.
"""

'''
Generator Expression We can easily create a generator expression without using user-defined function. It is the
same as the lambda function which creates an anonymous function; the generator's expressions create an anonymous
generator function.

The representation of generator expression is similar to the Python list comprehension. The only difference is that
square bracket is replaced by round parentheses. The list comprehension calculates the entire list, whereas the
generator expression calculates one item at a time.
'''

print("----------------------------------------------------------------------")

list_1 = [1, 2, 3, 4, 5, 6, 7]

# List Comprehension
z = [x ** 3 for x in list_1]
print(z)  # o/p : cubes of all list items in a list

# Generator expression
a = (x ** 3 for x in list_1)

print(a)  # o/p : gives object address of iterable
print("--------------------------------------------------------------------------------------")
"""
In the above program, list comprehension has returned the list of cube of elements whereas generator expression
has returned the reference of calculated value. Instead of applying a for loop, we can also call next() on the
generator object.
Let's consider another example:
"""

list_2 = [1, 2, 3, 4, 5, 6]

z = (x ** 3 for x in list_2)

print(next(z))

print(next(z))

print(next(z))

print(next(z))

print("------------------------------------------------------------------------------------")


# Example: Write a program to print the table of the given number using the generator.

def table(n):
    for i in range(1, 11):
        yield n * i
        # i = i + 1


for k in table(15):
    print(k)

"""
Advantages of Generators
There are various advantages of Generators. Few of them are given below:

1. Easy to implement
Generators are easy to implement as compared to the iterator. In iterator, we have to implement __iter__() and
__next__() function.

2. Memory efficient Generators are memory efficient for a large number of sequences. The normal function returns a
sequence of the list which creates an entire sequence in memory before returning the result, but the generator
function calculates the value and pause their execution. It resumes for successive call. An infinite sequence
generator is a great example of memory optimization. Let's discuss it in the below example by using
sys.getsizeof() function.

"""
print("-------------------------------------------------------------------------------------------")
import sys

# List comprehension
nums_squared_list = [i * 2 for i in range(10)]
print("Memory in Bytes:")
print(sys.getsizeof(nums_squared_list))
# Generator Expression
nums_squared_gc = (i ** 2 for i in range(10))
print("Memory in Bytes:")
print(sys.getsizeof(nums_squared_gc))

"""
We can observe from the above output that list comprehension is using 184 bytes of memory, whereas generator expression
is using 104 bytes of memory. It means that generator objects are much efficient than the list compression.

3. Pipelining with Generators
Data Pipeline provides the facility to process large datasets or stream of data without using extra computer memory.

Suppose we have a log file from a famous restaurant. The log file has a column (4th column) that keeps track of the
number of burgers sold every hour and we want to sum it to find the total number of burgers sold in 4 years. In that
scenario, the generator can generate a pipeline with a series of operations. Below is the code for it:

4. Generate Infinite Sequence

The generator can produce infinite items. Infinite sequences cannot be contained within the memory and since generators
produce only one item at a time, consider the following example:
"""
print("------------------------------------------------------------------------------------")


# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1
#
#
# for i in infinite_sequence():
#     print(i)

# generating fibonacci series by using generator function

def fib(num):
    a, b = 0, 1
    if a == 0 and b == 1:
        yield a
        yield b
    while True:
        c = a + b
        if c < num:
            yield c
            a = b
            b = c
        else:
            break


iterator = fib(15)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) # if we continue it throw error as num is upto 15


