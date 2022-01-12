"""
Decorators:
-----------
Decorators are a very powerful and useful tool in Python since it allows programmers to modify
the behaviour of function or class.
Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function,
without permanently modifying it.


Namespace and variable scope:
--------------------------------
namespace is a system which will control all the names in the program and it will allow us to reuse the name
in your program.
"""
# Ex:
x = 10
print(x)  # o/p 10
x = 11
print(x)  # o/p 11 and data 10 is garbage collected

"""
as above, while using same names there may be chance of loosing the data. while writing small programs
we can maintain unique names but while writing huge programs or importing modules we cannot check each name
whether it is unique to avoid loosing data. in this cases namespace comes to play, it will allow us to reuse
the names. there are different types of namespace:
      * built in namespace:
        when you start python interpreter, built in namespace is created, it contains all the
        built names.
      * global namespace:
        when we create any module that time it create its own global namespace, so each module
        has its own namespace. that's why we can use same names in different modules.
      * local namespace:
        when you call a function it creates a namespace called as local namespace.  

ex: if we are creating a fuction with same name in two different modules like
module1.py                             module2.py
def function():                        def function():
    pass                                   pass

we can call the above to functions like
module1.function()
module2.function()

"""
"""
variable scope:
---------------
part of a program where variable can be accessed is called as variable scope.
* local
* global
* enclosed
* builtin

* local scope:
--------------
  it contains the names defined inside the current function. if we declare any variable inside the function
  then the scope of the variable is inside the function. variables which are used in local scope are called
  as local variables.
* Global scope:
--------------- 
  it contains the names defined at the top level of the script or module. variables which are used in global
  scope are called as global variables.
* enclosed scope:
-----------------
  it contain names defined inside any and all enclosed function (nested function). variable declared in 
  enclosed scope are called as enclosed variable.
* built-in scope:
-----------------
  it contains the names built in to the python language through the special built in modules.

"""

y = 10  # it is global variable


def inner():
    x = 20  # it is local variable
    print('inner variable x: ', x)  # o/p: 20
    print('inner variable y: ', y)  # o/p: 10 we can access as it is global variable


print('outer variable y: ', y)  # o/p: 10
# print('outer variable x: ', x)  # o/p: error as we cannot access local variable outside the function
inner()

# modifying global variable in side function

y = 10  # it is global variable
print("================================================")


def inner():
    x = 20  # it is local variable
    global y  # to modify the global variable inside function we have to use this global keyword
    y = y + 1
    print('inner variable x: ', x)  # o/p: 20
    print('inner variable y: ', y)  # o/p: 11 we can access as it is global variable


print('outer variable y before calling inner(): ', y)  # o/p: 10
inner()
print('outer variable y after calling inner(): ', y)  # o/p: 11
print("================================================")

# modifying the enclosed variable

y = 50  # this global variable can be accessed anywhere but to modify inside func we use global keyword


def outer():
    x = 60  # in this case it is called as enclosed variable or nonlocal variable to inner()

    def inner():
        z = 100  # in this it is local variable
        nonlocal x  # we access enclosed variable inside nested func but to modify we use this nonlocal keyword
        x = x + 10
        print('inner value of z', z)  # o/p : 100
        print('inner value of y', y)  # o/p : 50
        print('inner value of x', x)  # o/p : 70

    inner()


outer()
print("================================================")

# LEGB rule

x = 10


def outer():  # enclosed function
    x = 20

    def inner():  # nested function
        x = 30

    inner()


outer()

# in the above program o/p will be 30 as it follows LEGB rule while executing.
# local --> enclosed --> golbal --> builtin

"""
closure:
--------
function object that remembers values in the enclosed scope even if they are not present in the memory. 

when do we have closure? or criteria to create a closure.
* nested function
* nested function must refer values in the enclosing scope
* enclosing function must return nested function

Advantages of closures
-----------------------
* can avoiding global values
* data hiding
* allows us implement decorators

"""


def outer():
    x = 3

    def inner():
        y = 3
        result = x + y
        return result

    return inner  # here outer function is returning inner function address


a = outer()  # here 'a' stores inner function address
print('calling inner function: ', a())  # here 'a' represents inner function

# in above using closure technique we have called the inner nested function from outside outer function.
# so, while calling inner function the object 'a' remembers the enclosed variable x and get executes
# for getting result

print("================================================")

"""
Decorators:
-----------
any callable object that is used to modify a function or class.
two types of decorators:
* function decorator
* class decorator

Criteria to create decorators:
* need to take function as parameter
* add functionality to function
* function need to be return another function

"""


#  function with out using decorator

def outer(func):
    def inner():
        st = func()
        return st.upper()

    return inner


def str():
    return 'hi shiva'


u = outer(str)  # without decorator should call outer() by passing the str address to convert string into upper case
print(u())

print("================================================")


# function using decorator

def outer(func):
    def inner():
        st = func()
        return st.upper()

    return inner


@outer
def str():
    return 'hi shiva'


print(str())
print("================================================")


# using decorator using parameters

def div(func):
    def inner(x, y):
        if y == 0:
            return "please give other than '0' number"
        return func(x, y)

    return inner


@div
def num(x, y):
    return x / y


print(num(4, 0))
print("================================================")


#  multiple decorators on single function

def outer_up(func):
    def inner_up():
        s1 = func()
        return s1.upper()

    return inner_up


def outer_split(func):
    def inner_split():
        s2 = func()
        return s2.split()

    return inner_split


@outer_split
@outer_up
def str():
    return 'hi shiva how are you'


print(str())

print("================================================")


# decorators with parameters

def deco_input(word):
    def outer_msg(func):
        def inner_msg():
            return func() + ' ' + word

        return inner_msg

    return outer_msg


@deco_input('shiva')  # passing parameter into function using decorator
def msg():
    return "good morning"


print(msg())

print("================================================")


# one decorator using on multiple functions

def outer_div(func):
    def inner_div(*args):
        l = []
        l = args[1:]
        for i in l:
            if i == 0:
                return "please don't enter value '0'"
        return func(*args)

    return inner_div


@outer_div
def div1(a, b):
    return a / b


@outer_div
def div2(a, b, c):
    return a / b / c


print(div1(10, 2))
print(div2(10, 0, 3))
print("================================================")
