from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import userProfile
from django.contrib.auth.models import User,auth
import os

# Create your views here.

def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(home)
        else:
            messages.success(request,'Login failed')
            return redirect(login)

    return render(request, 'login.html')
    
def registration(request):
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request,"User arleady exist")
                return redirect('registration')
            elif User.objects.filter(email = email).exists():
                messages.error(request,"Email arleady used")
                return redirect('registration')
            else:
                user=User.objects.create_user(username= username,password= password1, email= email, first_name= first_name, last_name= last_name)
                user.set_password(password1)
                user.save()
                messages.success(request,"Profile successfully created")
                return redirect('login')
    return render(request, 'registration.html')
    
def forgot(request):
    return render(request, 'forgot.html')

@login_required
# def profile(request):
    
#     profile=userProfile.objects.get(user=request.user)
#     if request.method=='POST':
#         profile.name = request.POST["name"]
#         profile.gender = request.POST["gender"]
#         profile.phone = request.POST["phone"]
#         profile.address = request.POST["address"]
#         profile.birthday = request.POST["birthday"]
#         profile.image = request.POST.get('image',None)
#         profile.save()
#     return render(request,'profile.html',locals())

# def logout(request):
#     auth.logout(request)
#     messages.success(request,'Logout Successfully')
#     return redirect(login)

def Profile(request):
    delete = request.GET.get('profile')
    if delete:
        delete_user = User.objects.get(id=delete)
        delete_user.delete()
        return redirect('login')

    a = request.user

    user1 = userProfile.objects.get(user=a)
    if request.method == 'POST':
        phn = request.POST.get('phn')
        birth = request.POST.get('birth')
        add = request.POST.get('add')
        img = request.FILES.get('img')

        if len(request.FILES) != 0:
            if len(user1.image) > 0:
                if user1.image != 'default.jpg':
                    os.remove(user1.image.path)
            user1.image = img
        user1.phone_number = phn
        user1.birthday = birth
        user1.address = add
        user1.save()
        return redirect('Profile')

    Context = {
        "user1": user1
    }
    return render(request, 'Profile.html', Context)
