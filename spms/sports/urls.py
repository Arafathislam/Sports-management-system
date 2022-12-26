from django.urls import path
from .import views


urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('news/',views.news,name="news"),
    path('register/',views.registration,name="register"),
    path('login/',views.login,name="login"),
    path('mail/',views.mail,name="mail"),
    path('contact/',views.contact,name="contact"),
    path('finalresult/',views.finalresult,name="finalresult"),
    path('tournament/',views.tournament,name="tournament"),
    path('teaminfo/',views.teaminfo,name="teaminfo"),
    path('allcard/',views.allcard,name="allcard"),
    path('admindash/',views.admindashboard,name="admindash"),
    path('payment/',views.payment,name="payment"),


]