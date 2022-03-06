from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'activities/home.html', {'posts': posts}) 

def about(request):
    return render(request, 'activities/about.html') 

def signup_user(request):
    if request.method == "GET":
        return render(request, "activities/signup.html")
    else:
        pass