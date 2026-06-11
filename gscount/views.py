from django.shortcuts import render, redirect
from django.http import HttpResponse

def team(request):
    return render(request, 'team.html')

def partner(request):
    return render(request, 'partner.html')

def style(request):
    return render(request, 'style.html')

def home(request):
    return render(request, 'home.html')

def upload(request):
    return render(request, 'upload.html')
