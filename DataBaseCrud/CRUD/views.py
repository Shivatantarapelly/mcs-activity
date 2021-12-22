from django.shortcuts import render, redirect

# Create your views here.
from CRUD.models import Register


def home(request):
    return render(request, 'index.html')


def savedata(request):
    name = request.POST['name']
    email = request.POST['email']
    pwd = request.POST['pwd']
    r1 = Register()
    r1.name = name
    r1.email = email
    r1.password = pwd
    r1.save()
    data = Register.objects.all()
    msg1 = True

    return render(request, 'showdata.html', {'data': data, 'msg1':msg1})


def readdata(request):
    data = Register.objects.all()
    msg = True
    return render(request,'showdata.html',{'data1': data, 'msg': msg})


def updatedata(request):
    return render(request,'update.html')


def update(request):
    name = request.POST['name']
    email = request.POST['email']
    pwd = request.POST['pwd']
    data = Register.objects.all()
    data.name = name
    data.email = email
    data.password = pwd
    data.save()
    return redirect('/')

