from django.shortcuts import render
from LOGINPAGE.templates.python import index
# Create your views here.

def createApp(request):
    return render(request, 'index.html')

def signIn(request):
    return index.signIn(request)

def signUp(request):
    return index.signUp(request)