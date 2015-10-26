from django.shortcuts import render
from django.db import models

class FoodTruck(models.Model):
    company = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)