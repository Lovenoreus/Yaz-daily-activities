from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'activities/home.html') 

def about(request):
    return render(request, 'activities/about.html') 