from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import authenticate, login, logout
from .models import Profile
# Create your views here.

def signup(request):
    return render(request, 'account/signUp.html')

def handlesignup(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        company = request.POST['company']
        designation = request.POST['designation']
        college = request.POST['college']
        tapas_batch = request.POST['tapas_batch']
        branch = request.POST['branch']
        year = request.POST['year']
        instagram = request.POST['instagram']
        linkedin = request.POST['linkedin']
        mail = request.POST['mail']
        main_image = request.FILES.get('image')
        if len(password) < 8:
            messages.error(request, "Password should be greater than 8 digits")
            return redirect('/Profile')
        if len(number) != 10:
            messages.error(request, "enter a valid number")
            return redirect('/Profile')
        checkemail = Profile.objects.filter(email=mail)
        if checkemail:
            messages.error(request, "e-mail already registered, please use a different id")
            return redirect('/Profile')
        try:
            user = User.objects.create_user(name,mail, password)
        except IntegrityError:
            messages.error(request, "Username already taken  please enter a unique Username")
            return redirect('/Profile')
        user.save()
        user = authenticate(request, username=name, password=password)
        profile = User.objects.filter(name= name)
        profile.main_image = main_image
        profile.company = company
        profile.designation = designation
        profile.branch = branch
        profile.year = year
        profile.tapas_batch = tapas_batch
        profile.college = college
        profile.instagram = instagram
        profile.linkedin = linkedin
        profile.mail = mail
        profile.save()
        messages.success(request,"your account has been created sucessfully")
        if user is not None:
            login(request,user)
            return redirect("/")
    else:
        return HttResponse('404')


def loginpage(request):
    return render(request, 'account/login.html')


def handeLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/account/login")

    return HttpResponse("404- Not found")

def handelLogout(request):
    logout(request)
    return redirect('/')
