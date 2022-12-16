from django.shortcuts import render

# Create your views here.

def home(request):
    context={}

    return render(request,'sports/main.html',context)

def about(request):
    contxt={}
    return render(request,'sports/about.html',context)

def news(request):
    context={}
    return render(request,'sports/news.html',context)


def registration(request):
    context={}
    return render(request,'sports/registration.html',context)

def login(request):
    context={}
    return render(request,'sports/Login.html',context)

