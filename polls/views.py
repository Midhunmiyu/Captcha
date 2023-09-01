from django.shortcuts import render, redirect
from django.conf import settings
import requests
from django.contrib import messages
from .forms import CaptchaForm
from django.http import HttpResponse

def list(request):
    return render(request,'view.html')

def index(request):
    # recaptcha_site_key = settings.RECAPTCHA_PUBLIC_KEY

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(name)
        print(email)
        messages.info(request,'Submitted form Successfully...!!')
        return redirect('list')
    
    return render(request, 'index.html')







