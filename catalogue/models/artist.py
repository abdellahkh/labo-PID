from django.db import models
# Create your models here.
class Artist(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    def __str__(self):
        return self.firstname +" "+ self.lastname
    class Meta:
        db_table = "artists"
