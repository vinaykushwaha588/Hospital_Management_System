from unicodedata import name
from django.urls import path
from .views import *
#BASEURL: http://127.0.0.1:8000/hms/

urlpatterns = [
    
    path('',view_home,name='home'),
    path('about/',view_about,name='about'),
    path('doctor/',view_doctor,name='doctor'),
    path('news/',view_news, name='news'),
    path('appointment/',view_appointment,name='appointment'),
    path('contact/',view_contact,name='contact'),
     
]


