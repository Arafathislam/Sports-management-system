from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import datetime
import json
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

    context={}
    return render(request,'sports/Teaminfo.html',context)

def admindashboard(request):
    context={}
    return render(request,'sports/admindashboard.html',context)


def allcard(request):
    context={}
    return render(request,'sports/AllCards.html',context)



def payment(request):
    transaction_id=datetime.datetime.now().timestamp()
    data=json.loads(request.body)
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        


    else:
        customer,order= guestOrder(request,data)

    total=float(data['form']['total'])
    order.transaction_id=transaction_id

    if total==order.get_cart_total:
        order.complete=True
    order.save()

    if order.shipping == True:
        ShippingAdderss.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],


        )
    # return JsonResponse('Payment complete !',safe=False)
    context={}
    return render(request,'sports/payment.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def room(request,pk):
    room=Room.objects.get(id=pk)
    room_messages=room.message_set.all().order_by('-created')
    participants=room.participants.all()
    if request.method == 'POST':
        message=Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room',pk=room.id)

    context= {'room':room , 'room_messages':room_messages ,'participants':participants}

    return render(request,'base/room.html',context)


def userProfile(request,pk):
    user=User.objects.get(id=pk)
    rooms=user.room_set.all()
    room_message=user.message_set.all()
    topics=Topic.objects.all()
    context={'user':user,'rooms':rooms,'room_message':room_message,'topics':topics}

    return render(request,'base/profile.html', context)