from django.shortcuts import render

# Create your views here.

def home(request):
    context={}

    return render(request,'sports/index.html',context)

def about(request):
    context={}
    return render(request,'sports/about.html',context)

def AllCards(request):
    context={}
    return render(request,'sports/AllCards.html',context)

def admindashboard(request):
    context={}
    return render(request,'sports/admindashboard.html',context)




