from django.shortcuts import render
from django.http import HttpResponse

def f_home_view(request):
    return render(request , "faculty/home.html")

def f_about_view(request):
    return render(request , "faculty/about.html",{'log':[i for i in range(4)]})

def login(request):
    return render(request, 'faculty/login.html')

def simple(request):
    return render(request, 'base2.html')