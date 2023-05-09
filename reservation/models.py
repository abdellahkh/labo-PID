from django.db import models

# Create your models here.

class Show(models.Model):
    slug = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=255)
    poster_url = models.CharField(max_length=255)
    locality_id = models.IntegerField()
    bookable = models.BooleanField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

