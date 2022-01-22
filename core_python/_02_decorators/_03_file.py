# @property decorator is used for calling any method as attribute outside class but
# when we want to modify that attribute from outside the function we have to use setter method


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @property  # this decorator is used to call the method as attribute out of the class
    def msg(self):
        return self.name + " got grade " + self.grade

    @msg.setter  # in this way we use the decorator as we want to set attribute msg so we use @msg.setter
    def msg(self, msg):
        message = msg.split(" ")
        print(message)
        self.name = message[0]
        self.grade = message[-1]


student = Student('shiva', 'A')  # here we pass shiva and A but o/p will be 'prasad got grade b'
student.msg = "Prasad got grade B"  # because here we are able to set the attribute using setter method
print('name:', student.name)
print('grade:', student.grade)
print('msg:', student.msg)  # here we are calling method as attribute outside class using obj reference
print("===================================================")


# if we want to modify private variables from outside class we can do by using getter and setter method


class Student:
    def __init__(self, marks):
        self.__marks = marks

    def percent(self):
        return (self.__marks / 600) * 100

    def setter(self, value):
        self.__marks = value

    def getter(self):
        return self.__marks


s = Student(400)
s.setter(500)
print(s.getter())
print(s.percent(), '%')
print("===================================================")


# in above we need to pass value to setter method and call getter method using object reference
# but with out using methods we have to modify and use by using attributes

class Student:
    def __init__(self, marks):
        self.__marks = marks

    def percent(self):
        return (self.__marks / 600) * 100

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if value < 0 or value > 600:
            print("value can't be set. value should be 0 to 600")
        else:
            self.__marks = value


s = Student(400)
s.marks = 500
print(s.marks)
print(s.percent(), '%')
print("===================================================")


# in the above we may confuse where to use @property.so to overcome that we can use property method in other way also

class Student:
    def __init__(self, marks):
        self.__marks = marks

    def percent(self):
        return (self.__marks / 600) * 100

    def getter(self):  # here method name came be anything
        return self.__marks

    def setter(self, value):  # here method name came be anything
        if value < 0 or value > 600:
            print("value can't be set. value should be 0 to 600")
        else:
            self.__marks = value

    marks = property(getter, setter)  # we can use property method like this for getting and setting variable


s = Student(400)
s.marks = 300
print(s.marks)
print(s.percent(), '%')
print("===================================================")


# @classmethods

class Student:
    counter = 0

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.counter += 1  # counting the number of times the object is created

    def msg(self):
        print(self.name + " got " + self.marks)

    @classmethod
    def object_count(cls):
        return cls.counter  # returning the count value of object created


s1 = Student('shiva', '96')
s2 = Student('sai', '97')
s3 = Student('prasad', '99')
print(Student.object_count())  # accessing class method using class name
print(s1.object_count())  # accessing class method using object

print("===================================================")


# modifying the instance variable using the class method

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def msg(self):
        print(self.name + " got " + self.marks, '%')

    @classmethod
    def get_per(cls, name, marks):
        return cls(name, str((int(marks) / 600) * 100))


s1 = Student('shiva', '96')
s2.msg()
marks = "550"      # modifying marks and name
name = "sai"
s2 = Student.get_per(name, marks)
s2.msg()
print("===================================================")

# @static method

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def msg(self):
        print(self.name + " got " + self.marks, '%')

    @classmethod
    def get_per(cls, name, marks):
        return cls(name, str((int(marks) / 600) * 100))

    @staticmethod
    def get_age(age):
        if age > 18:
            print('you are eligible for voting')
        else:
            print('you are not eligible for voting')


s1 = Student('shiva', '96')
Student.get_age(12)   # we can call method using class name
s1.get_age(25)      # we can call method using object

print("===================================================")

# pattern p-1
"""
*
* *
* * *
* * * *
"""
n = int(input('enter number of rows: '))
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end=' ')
    print()
print("======================= end p-1 ============================")

# pattern p-2

"""
*
* * *
* * * * *
* * * * * * *
"""

n = int(input('enter number of rows: '))
k = 1
for i in range(1, n+1):
    for j in range(1, k+1):
        print("*", end=' ')
    k += 2
    print()
print("======================= end p-2 ============================")

# pattern p-3

"""
    *
   * *
  * * *
 * * * *
"""

n = int(input('enter number of rows: '))
for i in range(0, n):
    for j in range(0, n-i-1):
        print(end=' ')
    for k in range(0, i+1):
        print("*", end=" ")
    print()
print("======================= end p-3 ============================")

# pattern p-4

"""
 * * * *
  * * *
   * *
    *
"""

n = int(input('enter number of rows: '))
for i in range(0, n):
    for j in range(0, i):
        print(end=' ')

    for k in range(0, n-i):
        print("*", end=" ")

    print()
print("======================= end p-4 ============================")

# pattern p-5

"""
    *
   * *
  * * *
 * * * *
  * * *
   * *
    *
"""

n = int(input('enter number of rows: '))
for i in range(0, n):
    for j in range(0, n-i-1):
        print(end=' ')
    for k in range(0, i+1):
        print("*", end=" ")
    print()

for i in range(1, n):
    for j in range(0, i):
        print(end=' ')

    for k in range(0, n-i):
        print("*", end=" ")

    print()
print("======================= end p-5 ============================")

# pattern p-6
"""
* * * *
* * *
* *
*
"""
n = int(input('enter number of rows: '))
for i in range(0, n+1):
    for j in range(0, n-i):
        print("*", end=' ')
    print()
print("======================= end p-6 ============================")

# pattern p-7
"""
   * * * 
 *       *
 *       *
 * * * * *
 *       *
 *       *
 *       *
 
"""
for row in range(7):
    for col in range(5):
        if row == 0 and (col == 0 or col == 4):
            print(" ", end=" ")
        elif col == 0 or col == 4 and row != 0:
            print("*", end=" ")
        elif row == 0 or row == 3 and col > 0 and col < 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("======================= end p-7 ============================")

