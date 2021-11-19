from django.test import TestCase
from django.db import models
from django import forms


# Create your tests here.
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
