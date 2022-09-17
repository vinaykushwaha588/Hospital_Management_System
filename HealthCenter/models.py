from ast import Not
from asyncio.windows_events import NULL
import email
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
dept_list=[
    ('Gerneral Helth','Gerneral Helth'),
    ('Cardiology','Cardiology'),
    ('Dental','Dental'),
    ('Dental','Dental'),
    ('Medical Research','Medical Research'),
]

class Appointment(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateField()
    dept = models.CharField(max_length=100,choices=dept_list)
    phone = models.CharField(max_length=15)
    msg = models.CharField(max_length=300)

    def __str__(self):
        return self.name