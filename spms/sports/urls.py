from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('login/',views.login,name='login'),
    path('forgotpass/',views.forgotpass,name='forgotpass'),
    path('registerAccount/',views.registerAccount,name='registerAccount'),
    # path('forgetpass/',views.forgetPass,name='forgetPass')


]