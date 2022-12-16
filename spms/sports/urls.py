from django.urls import path
from .import views


urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('news/',views.news,name="news"),
    path('register/',views.registration,name="register"),
    path('login/',views.login,name="login"),


]