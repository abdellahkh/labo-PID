from typing import Type
from django.db import models

class Artist(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    types = models.ManyToManyField(Type, through='ArtisteType')

    def __str__(self):
        return self.firstname + '' + self.lastname
    
    class meta: 
        db_table= "artists"