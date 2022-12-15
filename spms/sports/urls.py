from django.urls import path
from .import views


urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    
    path("AllCards", views.AllCards, name='AllCards'),
    path("admindashboard", views.admindashboard, name='admindashboard'),

]
