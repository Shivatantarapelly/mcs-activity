from django.shortcuts import render


# difference b/w cookies and session is cookies are store on client machine which can be access all the data
# from client machine where as session data is stored on server side and only session id is stored at client
# by which we can access data which is stored at server side

def setsession(request):
    request.session['course1'] = 'python'
    request.session['course2'] = 'java'
    request.session.set_expiry(600)

    return render(request, 'setsession.html')


#
# def getsession(request):
#     # name = request.session['course1']
#     name = request.session.get('course1', default='guest')
#
#     return render(request, 'getsession.html', {'name': name})

#
# def delsession(request):
#     if 'course1' in request.session:  # this is to check whether the key is present or not
#         del request.session['course1']
#     return render(request, 'delsession.html')


# getting all the keys and values of sessions

# def getsession(request):
#     name = request.session.get('course1')
#     keys = request.session.items()  # for getting key, value items
#     # keys = request.session.keys()  # for getting keys
#     age = request.session.setdefault('age', 26)
#     return render(request, 'getsession.html', {'name': name, 'keys': keys, 'age': age})


# deleting session using flush

def delsession(request):
    request.session.flush()
    return render(request, 'delsession.html')



def getsession(request):
    name = request.session.get('course1')
    print(request.session.get_session_cookie_age()) #getting session cookie age
    print(request.session.get_expiry_age())   # getting session expiry age
    print(request.session.get_expiry_date())  # getting session expiry date
    print(request.session.get_expire_at_browser_close())  # getting whether session closes if browser closes
    return render(request, 'getsession.html', {'name': name})
