from django.db import models

# Create your models here.
class Locality(models.Model):
    postal_code =  models.CharField(max_length=60)
    locality = models.CharField(max_length=60)
    
    class Meta:
        db_table = "localities"