from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'home.html')

def courses(request):
    return render(request,'course.html')

def bootcamp(request):
    return render(request,'bootcamp.html')

def requestCallBack(request):
    return render(request,'requestcall.html')