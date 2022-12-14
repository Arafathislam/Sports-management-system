from django.shortcuts import render

# Create your views here.

def home(request):
    context={}

    return render(request,'sports/index.html',context)

def about(request):
    contxt={}
    return render(request,'sports/about.html',context)


