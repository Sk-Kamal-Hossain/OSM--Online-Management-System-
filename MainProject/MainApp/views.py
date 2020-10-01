from django.shortcuts import render
from django.http import HttpResponse;
import sqlite3
from . import models 
# Create your views here.

def Index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def Reg_Done(request):
    regobj = models.Register()

    name = request.POST.get('name')
    mail = request.POST.get('mail')
    phone = request.POST.get('phone')
    psw = request.POST.get('psw')
    pswr = request.POST.get('pswr')

    #for register
    regobj.name = name
    regobj.mail = mail
    regobj.phone = phone
    regobj.psw = psw
    regobj.pswr = pswr
    regobj.save()

    all = [name, mail, phone, psw, pswr]
    return render(request, 'Reg_Done.html', {'all':all})

def login_done(request):
    #logobj = models.Login()

    #email = request.POST.get('email')
    #password = request.POST.get('password')


    #for login
    #logobj.email = email
    #logobj.password = password
    #logobj.save()

    #all = [email, password]
    return render(request, 'login_done.html')

def shoping_cart(request):
    return render(request, 'shoping_cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def profile(request):
    return render(request, 'profile.html')

def contact(request):
    return render(request, 'contact.html')