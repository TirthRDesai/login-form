from django.urls import path
from . import views


urlpatterns = [
    path('', views.transfer),
    path('LOGINPAGE/', views.createApp, name = 'homepage'),
    path('checkData/SignUp', views.signUp, name = 'signUp'),
    path('checkData/SignIn', views.signIn, name = 'signIn')
]
