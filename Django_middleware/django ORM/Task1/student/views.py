from django.shortcuts import render
from .models import Student, Teacher
from django.db import connection
from django.db.models import Q


def student_list(request):
    posts = Student.objects.all()

    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})


def student_list(request):
    posts = Student.objects.filter(surname__startswith='austin') | Student.objects.filter(surname__startswith='baldwin')

    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})


# Q is objects used for creating more complex queries which can combines |'s and &'s


def student_list(request):
    posts = Student.objects.filter(
        Q(surname__startswith='austin') | ~Q(surname__startswith='baldwin') | Q(surname__startswith='avery-parker'))

    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})


# using AND query

def student_list(request):
    posts = Student.objects.filter(surname__startswith='austin') & Student.objects.filter(age='20')

    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})


#  using Q object we can write query as below

def student_list(request):
    posts = Student.objects.filter(Q(surname__startswith='austin') & Q(age='20'))

    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})


# Using UNION query to combine the result sets of two or more select statements

def student_list(request):
    posts = Student.objects.all().values_list('firstname').union(Teacher.objects.all().values_list('firstname'))
    # the above query selects all teacher, students firstname with out duplicates
    # in above query values_list() will return values in list format. if we use values() then it returns in dic format
    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})


# using NOT query by exclude(<condition>) or filter(~Q(<condition>))

def student_list(request):
    posts = Student.objects.exclude(age=20) & (Student.objects.exclude(firstname__startswith='lakisha'))
    #  in above exclude will select the data which does not satisfy the condition and will not select other data

    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})


def student_list(request):
    posts = Student.objects.exclude(age__gt=20)
    # gt ==> greater than
    # gte ==> greater than and equal
    # lt ==> lesser than
    # lte ==> lesser than and equal

    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})


# we can use ~Q objects for exclude

def student_list(request):
    posts = Student.objects.filter(~Q(age__gt=20))

    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})


def student_list(request):
    posts = Student.objects.filter(~Q(age__lt=20) & ~Q(firstname__startswith='lakisha'))

    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})


# selecting individual fields for output

def student_list(request):
    posts = Student.objects.filter(classroom=2).only('firstname') # gives only firstname as o/p

    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})


# performing raw sql queries

def student_list_(request):
    posts = Student.objects.raw("SELECT * FROM student_student")

    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})


