from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('login/',views.login,name='login'),
    path('forgotpass/',views.forgetpass,name='forgotpass')
    # path('forgetpass/',views.forgetPass,name='forgetPass')


]