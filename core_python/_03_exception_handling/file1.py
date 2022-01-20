'''
Errors in python are three types
1. compile time error
2. Run time error
3. Logical error

compile time errors are nothing but syntax error which occurs when we not follow indentation, : etc
fails to compile. these error are detected by python compiler

runtime error are occurred when pvm is not able to execute some statement in the program. these error
is detected by pvm at run time only

logical errors occur due to flaws in logic of the program. logical errors are not detected by pvm or
python compiler as it logical code mistake made by programmer and programmer is responsible for it.

Exception:
Exceptions are the unusual event that occurs during the execution of the program that interrupts the
normal flow of the program.
Generally, exceptions occur when the code written encounters a situation it cannot cope with.
Whenever an exception is raised, the program stops the execution, and thus the further code is not executed.
Therefore, an exception is a python object that represents a run-time error.
An exception is a Python object that represents an error.
To handle the exceptions we use Try and except block
 The try block has the code to be executed and if any exception occurs then the action to perform is written
 inside the Except block.

 syntax:
 try:
    statements to be executed
 except:
    statements to be executed if exception occurs
'''

# P-1
try:
    a = int(input('enter a number:'))  # these statements are executed first
    b = int(input('enter a number'))  # if user enters invalid details it goes to except block


    def sum(x, y):
        res = x + y
        return res


    sum(a, b)

except ValueError:
    print('enter only numbers')  # this statement will get execute and user get message of enter num only

print('---end of the program---')  # whether exception occurs or not this statement will execute as we are handling the
# the exception


print('=================end P-1========================')

# P-2
'''
we can use one try block with multiple except blocks. if try block doesn't throw exception the except block will
not execute. if it throws the exception then the except block with specific error will execute
'''
try:
    x = int(input('enter a number'))
    l = [10, 20, 26, 41, 33, 25, 44]
    l1 = []

    for i in l:
        if i % x == 0:
            l1.append(i)
        else:
            pass
    print('the value in list which are exactly divisble by given number:', l1)

except ValueError:
    print('enter numbers only')

except ZeroDivisionError:
    print("Don't enter zero")

except Exception as e:
    print('unexpected Error')

print('=================end P-2========================')

# P-3
'''

we can use finally at the end of all blocks to close files or like database connections.
whether the exception occur or not the statement in the finally block will get executed
'''

try:
    z = open('E:\hrcallmynotes', 'r')

except FileNotFoundError:
    print('file has not found')

finally:
    print('---file has been closed---')

print('=================end P-3========================')

# P-4
'''
we can use multiple except blocks with one try block at start and ending with one finally block

'''

try:
    x = int(input('enter a number: '))
    l = []
    for i in range(5):
        res = i / x
        l.append(res)
    print(l)

    z = open('E:\hrcallmynotes', 'r')

except ValueError:
    print('enter only numbers')

except ZeroDivisionError:
    print("please don't enter Zero ")

except FileNotFoundError:
    print('file has not found')

finally:
    print('---file has been closed---')

print('=================end P-4 ========================')

# p-5
'''
we can use else block with try and except block or with one try block also. else block should
be used after all except blocks and before finally block.
if the try block throws the exception then the statements in respective exception handling block
will get executed or if try block doesn't throws a exception and code in try block executed successfully
then all the statements in the else block will be getting executed.
'''

try:
    x = int(input('enter a number:'))

except ValueError:
    print('enter valid input')

else:
    l = []
    for i in range(x):
        l.append(i)
    print(l)

finally:
    print('---file has closed---')  # the statements written here will be get executed either exception occurs or not

print('=================end P-5 ========================')

# P-6

'''
we can use multiple try and multiple except blocks according to our logic

'''

try:
    x = int(input('enter a number:'))
except ValueError:
    print('enter valid number')
l1 = []
l2 = []
try:
    for i in range(x):
        l1.append(i)
    print(l1)
except NameError:
    print('You have passed string instead of number')
try:
    for i in range(len(l1)):
        x = l1[i] * 2
        l2.append(x)
    print(l2)
except IndexError:
    print('you have missed the logic')

except Exception:
    print('Unexpected error')

finally:
    print('--- program ended ---')

print('=================end P-6 ========================')

# P-7

# we can use one try with multiple except and then else and at end we can use finally block

print("press '0' to add number or '1' to add any two strings")
try:
    def inp(x):
        if x == 0:
            num1 = int(input('enter a number:'))
            num2 = int(input('enter a number:'))
            return num1, num2
        elif x == 1:
            string1 = str(input('enter a string:'))
            string2 = str(input('enter a string:'))
            return string1, string2
        else:
            print('please enter valid option only')
            return inp(int(input('enter 0 or 1 : ')))


    A, B = inp(int(input('enter your choice 0 or 1:')))
except ValueError:
    print('Please enter valid input:')
    print("press '0' to add number or '1' to add any two strings")
    A, B = inp(int(input('enter your choice 0 or 1:')))


    def add(a, b):
        if type(a) == int and type(b) == int:
            print('Addition of two integers:', a + b)
        if type(a) == str and type(b) == str:
            print('Addition of two strings:', a + b)


    add(A, B)
except Exception:
    print('Please enter valid input:')
    print("press '0' to add number or '1' to add any two strings")
    A, B = inp(int(input('enter your choice 0 or 1:')))


    def add(a, b):
        if type(a) == int and type(b) == int:
            print('Addition of two integers:', a + b)
        if type(a) == str and type(b) == str:
            print('Addition of two strings:', a + b)


    add(A, B)


else:
    def add(a, b):
        if type(a) == int and type(b) == int:
            print('Addition of two integers:', a + b)
        if type(a) == str and type(b) == str:
            print('Addition of two strings from else:', a + b)


    add(A, B)

finally:
    print('---end of the program----')

print('=================end P-7 ========================')

'''
we can raise the exception where we want inside the try block and when the raise statement executes
the statements inside the concerned exception block will get executed
'''


# P-8

def add():
    try:
        age = int(input('enter a number:'))
        if age < 0:
            raise ValueError('please enter number above 0')
        elif age > 100:
            raise OverflowError('please enter below 100')
        elif age < 18:
            print('you are not eligible to vote')
        elif age >= 18:
            print('you are eligible to vote')
        else:
            pass
    except ValueError as v:
        print(v)
        add()
    except OverflowError as o:
        print(o)
        add()
    except Exception as e:
        print('unexpected error')
        add()


add()

print('=================end P-8 ========================')

'''
we create our own exception class and can use our own modified exception by simply raising with
exception class when ever required.
'''


# P-9

class Shiva(Exception):
    def __init__(self, e):
        self.e = e
        print(self.e)


def add():
    try:
        num1 = int(input('enter a number:'))
        num2 = int(input('enter a number:'))
        if num1 < 0 or num2 < 0:
            raise Shiva('please enter both number greater than zero')

        else:
            print(num1 + num2)
    except ValueError:
        print('enter number only')
        add()
    except Shiva:
        add()


add()

print('=================end P-8 ========================')
