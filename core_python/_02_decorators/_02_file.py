# class decorators
#  using function decorator on class method
def check_name(func):
    def inner(name_ref):
        if name_ref.name == 'shiva':
            print(" hey my name is also same")
        else:
            func(name_ref)

    return inner


class Name:
    def __init__(self, name):
        self.name = name

    @check_name
    def print_name(self):
        print('entered name is: ', self.name)


# N = Name(str(input('enter your name: ')))
N = Name('shiva')
N.print_name()
print("===================================================")


# call method
class Name:
    def __init__(self, name):
        self.name = name

    def __call__(self):  # this call method is a special method executes whenever object is called like N()
        print('entered name is: ', self.name)


# N = Name(str(input('enter your name: ')))
N = Name('shiva')
N()  # with out using call method in class we get error that object is not call able
print("===================================================")


# using  class decorator on function

class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        st = self.func()
        return st.upper()


@Decorator
def msg():
    return "good morning shiva"


print(msg())
print("===================================================")


class Div:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        l = []
        l = args[1:]
        for i in l:
            if i == 0:
                return "please don't enter value '0'"
        return self.func(*args, **kwargs)


@Div
def div1(a, b):
    return a / b


@Div
def div2(a, b, c):
    return a / b / c


print(div1(10, 20))
print(div2(10, 0, 20))

print("===================================================")


# built in decorators:
#      @property decorator
#      @class decorator
#      @static decorator

# using class methods as attributes using @property decorator

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @property       # this decorator is used to call the method as attribute out of the class
    def msg(self):
        return self.name + " got grade " + self.grade


student = Student('shiva', 'A')
student.grade = 'B'
print('name:', student.name)
print('grade:', student.grade)
print('msg:', student.msg)    # here we are calling method as attribute outside class using obj reference
print("===================================================")



