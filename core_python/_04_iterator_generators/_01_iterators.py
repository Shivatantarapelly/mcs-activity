"""
Python Iterators
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods
__iter__() and __next__().

Iterator vs Iterable
Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an
iterator from.

All these objects have a iter() method which is used to get an iterator:

Example
Return an iterator from a tuple, and print each value:

"""
my_tuple = ("apple", "banana", "cherry")
my = iter(my_tuple)

print(next(my))
print(next(my))
print(next(my))
# print(next(my))    # here it throws error stop iteration as there are no items to get iterated

print("----------------------------------------------------------------")
"""
Even strings are iterable objects, and can return an iterator:

Example
Strings are also iterable objects, containing a sequence of characters:
"""
my_str = "banana"
myit = iter(my_str)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

"""
Looping Through an Iterator
We can also use a for loop to iterate through an iterable object:

Example
Iterate the values of a tuple:
"""
print("------------------------------------------------")
#  The for loop actually creates an iterator object and executes the next() method for each loop.
my_tuple = ("apple", "banana", "cherry")

for x in my_tuple:
    print(x)

"""
Create an Iterator
To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), 
which allows you to do some initializing when the object is being created. 

The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator 
object itself.

The __next__() method also allows you to do operations, and must return the next item in the sequence.

Example
Create an iterator that returns numbers, starting with 1, and each sequence will increase by one 
(returning 1,2,3,4,5 etc.):
"""
print("------------------------------------------------------------------------------------")


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 2
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

"""
StopIteration
The example above would continue forever if you had enough next() statements, or if it was used in a for loop.

To prevent the iteration to go on forever, we can use the StopIteration statement.

In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified 
number of times:

Example
Stop after 20 iterations:
"""
print("------------------------------------------------------------------------------")


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

print("------------------------------------------------------------------------------")


# writing a function to pass a iterable into function which returns the items in iterable

def iterate(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        else:
            print(item)


iterate([15, 36, 'shiva', 15.6])

print("------------------------------------------------------------------------------")


# printing 2 power of values upto the max number which we give as input

class MyIter:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


for i in MyIter(5):
    print(i)
