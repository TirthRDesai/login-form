from django.urls import path
from . import views


urlpatterns = [
    path('', views.transfer),
    path('LOGINPAGE/', views.createApp, name = 'homepage'),
    path('LOGINPAGE/checkData/SignUp', views.signUp, name = 'signUp'),
    path('LOGINPAGE/checkData/SignIn', views.signIn, name = 'signIn')
]
