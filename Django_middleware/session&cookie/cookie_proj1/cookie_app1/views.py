from datetime import datetime, timedelta

from django.shortcuts import render

# Create your views here.

def setcookie(request):
    response = render(request, 'student/setcookie.html')
    response.set_cookie('name', 'shiva')
    return response


def getcookie(request):
    # name = request.COOKIES['name']
    #  if we use above when the cookies doesn't exits then it returns error.
    #  by using below we can get default value as none
    # name = request.COOKIES.get('name')
    # by using below way we get the value if cookie exist or else the value which is given is replaced
    name = request.COOKIES.get('name', 'sai')
    return render(request, 'student/getcookie.html', {'name': name})


def delcookie(request):
    response = render(request, 'student/delcookie.html')
    response.delete_cookie('name')
    response.delete_cookie('shiva')
    return response


def setcookie1(request):
    response = render(request, 'student/setcookie.html')
    response.set_cookie('hello', 'world', max_age=30)  # after 30sec cookie will deleted
    response.set_cookie('shiva', 'prasad', expires=datetime.utcnow() + timedelta(days=2))
    # above is used to set cookies for 2days than get deleted
    return response
"""

# creating signed cookieby using set_signed_cookie() which provides security value


def setcookie(request):
    response = render(request, 'student/setcookie.html')
    response.set_signed_cookie('name', 'shiva', salt='nm')
    # in above salt provides security and will get only if the salt matches while getting cookie
    return response


def getcookie(request):
    name = request.get_signed_cookie('name', default='sai', salt='nm')
    # in above salt should matche or else it shows error
    return render(request, 'student/getcookie.html', {'name': name})


def delcookie(request):
    response = render(request, 'student/delcookie.html')
    response.delete_cookie('name')
    return response
"""
