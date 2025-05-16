# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse("Hello WOrld")
    return render(request, 'home.html')

def posts(request):
    #return HttpResponse("Hello WOrld")
    return render(request, 'posts.html')

def sobre(request):
    #return HttpResponse("Hello WOrld")
    return render(request, 'about.html')