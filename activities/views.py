from django.shortcuts import render, redirect
from .models import Post, CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login ,authenticate, logout
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
import re

# Create your views here.
def home(request):
    posts = Post.objects.all()
    list1 = [2,3]
    return render(request, 'activities/home.html', {'posts': posts}) 

def about(request):
    return render(request, 'activities/about.html') 

def signup_user(request):
    if request.method == "GET":
        return render(request, "activities/signup.html", {"form":UserCreationForm()})
    else:
        print(request.POST["email"][0])
        if request.POST["password1"] != request.POST["password2"]:
            return render(request, "activities/signup.html", {"form":UserCreationForm(), "error":"Passwords don't match"})
        
        if bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", request.POST["email"])) == False:
            return render(request, "activities/signup.html", {"form":UserCreationForm(), "error":"You have entered an invalid email address"})

        try:
            user = CustomUser.objects.create_user(request.POST["username"], password=request.POST['password1'],email=request.POST['email'])
            user.save()
            login(request, user)
            return redirect('home')
        except IntegrityError: 
            return render(request, 'activities/signup.html',{"form": UserCreationForm(), "error": "That username or email has already been used"})
'''
from django.contrib.auth import update_session_auth_hash

def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
'''
def login_user(request):
    if request.method == "GET":
        return render(request, "activities/login.html")
    else:
        print(bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", request.POST["emailorusername"])))
        if bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", request.POST["emailorusername"])):
            try:
                username1 = CustomUser.objects.get(email=request.POST["emailorusername"]).username
                user = authenticate(request, username= username1, password=request.POST["password"])
            except ObjectDoesNotExist:
                return render(request, 'activities/login.html',{"error": "Invalid Information"})
        else:
            user = authenticate(request, username=request.POST["emailorusername"], password=request.POST["password"])
        
        if user is None:
            return render(request, 'activities/login.html',{"error": "Invalid Information"})
        else:
            login(request, user)
            return redirect('home')

def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")
