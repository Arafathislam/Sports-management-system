from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    return render(request,'sports/index.html')
def about(request):
    return render(request,'sports/about.html')

def login(request):
    return render(request,'sports/login.html')

def forgotpass(request):
    return render(request,'sports/forgotpass.html')

def registerAccount(request):
    form=UserCreationForm()
    context={'form':form}
    return render(request,'sports/registerAccount.html',context)




