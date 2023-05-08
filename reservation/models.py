from django.db import models

# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length=70)
    lastName = models.CharField(max_length=70)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

