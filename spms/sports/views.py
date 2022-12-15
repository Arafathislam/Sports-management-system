from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'sports/index.html')
def about(request):
    return render(request,'sports/about.html')

def login(request):
    return render(request,'sports/login.html')

def forgetpass(request):
    return render(request,'sports/forgotpass.html')




