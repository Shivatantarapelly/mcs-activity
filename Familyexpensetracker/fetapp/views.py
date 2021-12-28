from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
# Create your views here.
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from Familyexpensetracker import settings
from fetapp.models import Add_New_Expenses, Add_new_member
from fetapp.tokens import generator_token


def home1(request):
    return render(request, 'authentication/index.html')


def home(request):
    ndata = Add_New_Expenses.objects.all()
    return render(request, "Home.html", {'data': ndata})


def signup(request):
    if request.method == 'POST':
        # username = request.POST.get('uname')  or
        username = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        if User.objects.filter(username=username):
            messages.error(request, "username already exist, try with other username")
            return redirect('/signup')

        if User.objects.filter(email=email):
            messages.error(request, "Email already exist, try with other Email")
            return redirect('/signup')
        if password1 != password2:
            messages.error(request, "password didn't match")
            return redirect('/signup')
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()
        messages.success(request, "your account has been successfully created, please check mail to activate through "
                                  "confirmation email")

        # for 1st email

        subject = "welcome to Family Expense Tracker app"
        message = "Hello" + "" + myuser.first_name + "!! \n" + "Welcome to family expense tracker app \n" + \
                  "We have also sent confirmation email. Please confirm the email address to activate your account." \
                  "\n\n\n Thank You, \n Shiva."
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        # email confirmation
        current_site = get_current_site(request)
        email_subject = "confirm your email"
        message2 = render_to_string("email_confirmation.html", {
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generator_token.make_token(myuser)
        })
        email = EmailMessage(email_subject, message2, settings.EMAIL_HOST_USER, [myuser.email], )
        email.fail_silently = True
        email.send()

        return redirect('/signin')
    return render(request, 'authentication/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            ndata = Add_New_Expenses.objects.all()
            context = {'user': user, 'data': ndata}

            return render(request, "Home.html", context)

        else:
            messages.error(request, "Invalid Credentials!")
            return redirect('/signin')
    return render(request, 'authentication/signin.html')


def signout(request):
    return redirect('/')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generator_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('/')
    else:
        return render(request, 'activation_fail.html')


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
