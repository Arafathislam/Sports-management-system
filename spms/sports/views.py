from django.shortcuts import render

# Create your views here.

def home(request):
    context={}

    return render(request,'sports/main.html',context)

def about(request):
    context={}
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

def mail(request):
    context={}
    return render(request,'sports/mail.html',context)


def contact(request):
    context={}
    return render(request,'sports/contact.html',context)


def finalresult(request):
    context={}
    return render(request,'sports/Final_Result.html',context)


def tournament(request):
    context={}
    return render(request,'sports/tournament.html',context)

def teaminfo(request):
    context={}
    return render(request,'sports/Teaminfo.html',context)

def admindashboard(request):
    context={}
    return render(request,'sports/admindashboard.html',context)


def allcard(request):
    context={}
    return render(request,'sports/AllCards.html',context)


