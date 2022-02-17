from django.shortcuts import render, HttpResponse


# Create your views here.
def setsession(request):
    request.session['name'] = 'shiva'
    return render(request, 'setsession.html')


def getsession(request):
    if 'name' in request.session:
        name = request.session['name']
        request.session.modified = True
        return render(request, 'getsession.html', {'name': name})
    else:
        return HttpResponse("your session got expired....")


def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'delsession.html')
