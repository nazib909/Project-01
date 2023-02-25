#from django.shortcuts import renderfrom django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from app.models import userProfile
from django.contrib.auth.models import User,auth

def home(request):
    return render(request, 'home.html')