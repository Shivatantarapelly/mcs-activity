from django.shortcuts import render, redirect

# Create your views here.
from fetapp.models import Add_New_Expenses, Add_new_member


def home(request):
    ndata = Add_New_Expenses.objects.all()
    return render(request, "Home.html", {'data': ndata})


def add(request):
    mlist = Add_new_member.objects.values_list('Name', flat=True)
    return render(request, "Addeditexpense.html", {'mlist': mlist})


def viewmember(request):
    return render(request, "Addeditmember.html")


def addexpense(request):
    if request.method == 'POST':
        eid = request.POST['Eid']
        name = request.POST['Name']
        purpose = request.POST['Purpose']
        amount = request.POST['Amount']
        date = request.POST['Date']
        data = Add_New_Expenses()
        data.Eid = eid
        data.Name = name
        data.Purpose = purpose
        data.Amount = amount
        data.Date = date
        data.save()
        # ndata = Add_New_Expenses.objects.all()
        # return render(request, "Home.html", {'data': ndata})
        response = redirect('/home')
        return response


def addmember(request):
    if request.method == 'POST':
        mid = request.POST['Mid']
        a_name = request.POST['Name']
        mobile_no = request.POST['Number']
        work = request.POST['Work']
        income = request.POST['Income']
        data = Add_new_member()
        data.Mid = mid
        data.Name = a_name
        data.Mobile_no = mobile_no
        data.Work = work
        data.Income = income
        data.save()
        mdata = Add_new_member.objects.all()
        return render(request, "Family.html", {'mdata': mdata})


def editexpense(request, id):
    ndata = Add_New_Expenses.objects.get(Eid=id)
    return render(request, 'Addeditexpense.html', {'edata': ndata})


def update(request, id):
    if request.method == 'POST':
        eid = request.POST['Eid']
        name = request.POST['Name']
        purpose = request.POST['Purpose']
        amount = request.POST['Amount']
        date = request.POST['Date']
        editdata = Add_New_Expenses.objects.get(Eid=id)
        editdata.Eid = eid
        editdata.Name = name
        editdata.Purpose = purpose
        editdata.Amount = amount
        editdata.Date = date
        editdata.save()
        return redirect('/home')


def deleteexpense(request, id):
    data = Add_New_Expenses.objects.get(Eid=id)
    data.delete()
    return redirect('/home')


def viewfamily(request):
    data = Add_new_member.objects.all()
    return render(request, 'viewfamily.html', {'data': data})


def deletemem(request, id):
    data = Add_new_member.objects.get(Mid=id)
    data.delete()
    return redirect('/viewfamily')


def editmem(request, id):
    ndata = Add_new_member.objects.get(Mid=id)
    return render(request, 'Addeditmember.html', {'edata': ndata})


def updatemem(request, id):
    if request.method == 'POST':
        mid = request.POST['Mid']
        name = request.POST['Name']
        mobileno = request.POST['Mobile_no']
        work = request.POST['Work']
        income = request.POST['Income']
        editmem = Add_new_member.objects.get(Mid=id)
        editmem.Eid = mid
        editmem.Name = name
        editmem.Mobile_no = mobileno
        editmem.Work = work
        editmem.Income = income
        editmem.save()
        return redirect('/viewfamily')


def addnewmem(request):
    page = redirect('/viewmember')
    return page


def redhome(request):
    page = redirect('/home')
    return page
