from django.db import models

class Locality(models.Model):
    name = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
   