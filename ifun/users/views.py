from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.contrib import auth
# Create your views here.


def signin(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'GET':
        return render_to_response('users/signin.html', c)
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            return HttpResponse('logined')
        else:
            return HttpResponse('invalid')


def signup(request):
    if request.method == 'GET':
        return render(request, 'users/signup.html')
    else:
        return HttpResponse('hello post')
