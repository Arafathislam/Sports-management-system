from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import datetime
import json
from . utils import cookieCart ,cartData,guestOrder
from django.views.decorators.csrf import csrf_exempt


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
       page='register'
    form=MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')

        else:
            messages.error(request,'An error occured during registration')

    context={'form':form}
    return render(request,'sports/registration.html',context)

def login(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password=request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request,'User doesnot exit')

        user=authenticate(request,email=email,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
             messages.error(request,'Username or Password exit')

    context={'page':page}
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
    q=request.GET.get('q')if request.GET.get('q')!=None else ''
    topics=Topic.objects.filter(name__icontains=q)
    context={}
    return render(request,'sports/Teaminfo.html',context)

def admindashboard(request):
    context={}
    return render(request,'sports/admindashboard.html',context)


def allcard(request):
    context={}
    return render(request,'sports/AllCards.html',context)

def scorebordrequest):
    mydata = members.objects.all()
    mydata2 = members.objects.all()
    mydata3 = members.objects.all()
    template = loader.get_template('C:football.html')
    context = {
        'mymembers': mydata ,
        'mymembers2': mydata2 ,
        'mymembers3': mydata3 ,
    }
    return HttpResponse(template.render(context,request))


