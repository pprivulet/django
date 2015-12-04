from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def signin(request):
    if request.method == 'GET':
        return render(request, 'users/signin.html')
    else:
        HttpResponse('hello post') 


def signup(request):
    HttpResponse('hello signup')
