from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .forms import SignUpForm
from django.core.mail import send_mail
from django.conf import settings
EMAIL_HOST_USER = settings.EMAIL_HOST_USER
from django.contrib.auth.models import User
from django.http import HttpResponse

@login_required
def home(request):
    return render(request, "home.html", {})

def authView(request):
    if request.method == "POST":
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            print("user created", form.data)
            return redirect("base:login")
        else:
            print("form is not valid", form.errors)
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})

def profile(request):
    return render(request, "profile.html", {})

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("base:home")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "change_password.html", {"form": form})

def custom_logout(request):
    logout(request)
    return redirect("/accounts/login/")

def ForgetPassword(request):
    if request.method == "POST":
        email = request.POST.get("email")
        print("Email: ", email)
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            print("user exist")
            send_mail("Reset your password: ", f"Hey User: {user}! To reset password, click on the given link \n http://127.0.0.1:8000/newpasswordpage/{user}/", EMAIL_HOST_USER, [email], fail_silently=False)
            return HttpResponse("<h3>password reset link sent to your email!!</h3>")
            
        return render(request, "registration/forget_password.html")
    return render(request, "registration/forget_password.html")
    
        
def NewPasswordPage(request, user):
    userid = User.objects.get(username=user)
    print("userid: ", userid)
    if request.method == "POST":
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")
        
        print("pass1 and pass2: ", pass1, pass2)
        if pass1 == pass2:
            userid.set_password(pass1)
            userid.save()
            return redirect("/accounts/login/")
        
    return render(request, "registration/new_password.html")        
