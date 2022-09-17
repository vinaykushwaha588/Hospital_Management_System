from django.http import HttpResponse
from django.shortcuts import render
from .models import Appointment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
# Create your views here.

def view_home(request):
    resp=render(request,'HealthCenter/home.html')
    return resp

def view_about(request):
    resp=render(request,'HealthCenter/about.html')
    return resp

def view_doctor(request):
    resp=render(request,'HealthCenter/doctor.html')
    return resp

def view_news(request):
    resp=render(request,'HealthCenter/news.html')
    return resp

# @login_required
def view_appointment(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        date =request.POST.get('date')
        dept = request.POST.get('select')
        phone = request.POST.get('phone')
        msg = request.POST.get('message')
        data=Appointment(name=name,email=email,date=date,dept=dept,phone=phone,msg=msg)
        data.save()
        # print(name,email,date,phone,msg)

    resp=render(request,'HealthCenter/appointment.html')
    return resp

def view_contact(request):
    resp=render(request,'HealthCenter/contact.html')
    return resp

