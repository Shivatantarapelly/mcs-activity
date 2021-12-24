from django.contrib.auth import authenticate, login
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.encoding import force_bytes, force_text
from .tokens import generator_token

# Create your views here.
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from GFG import settings


def home(request):
    return render(request, 'authentication/index.html')


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
        if not username.isalnum():
            messages.error(request, "username must be alphanumeric")
            return redirect('/signup')

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()
        messages.success(request, "your account has been successfully created. we have sent confirmation mail. please "
                                  "confirm in order to activate account")
        # email code

        subject = "welcome to my app"
        message = "hello" + myuser.first_name + "!! \n" + "welcome to you app \n" + "we have also sent confirmation " \
                                                                                    "email, Please confirm your email " \
                                                                                    "addresss in order to activate your " \
                                                                                    "account \n\nThank you\n shiva "
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
            context = {'user': user}
            return render(request, "authentication/loggedin.html", context)
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
