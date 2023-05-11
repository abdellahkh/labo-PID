from django.db import models

# Create your models here.


class Locality(models.Model):
    postal_code = models.CharField(max_length=6)
    locality = models.CharField(max_length=60)
    
    def __str__(self):
        return self.locality


class Location(models.Model):
    slug = models.CharField(max_length=60)
    designation = models.CharField(max_length=60)
    address = models.CharField(max_length=255)
    locality_id = models.ForeignKey(Locality, blank=True, null=True, on_delete=models.CASCADE)
    website = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.slug


class Show(models.Model):
    slug = models.CharField(max_length=60)
    title = models.CharField('Show Title', max_length=255)
    description = models.TextField('Show Description')
    poster_url = models.CharField('Show Image', max_length=255)
    location_id = models.ForeignKey(Location, blank = True, null = True, on_delete=models.SET_NULL)
    bookable = models.BooleanField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.slug

class Artist(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)

    def __str__(self):
        return self.firstname + '' + self.lastname

class Type(models.Model):
    type= models.CharField(max_length=60)

    def __str__(self):
        return self.type


class ArtisteType(models.Model):
    artist_id = models.ForeignKey(Artist, blank = True, null = True, on_delete=models.CASCADE)
    type_id = models.ForeignKey(Type, blank=True, null=True, on_delete=models.CASCADE)


class ArtistTypeShow(models.Model):
    artiste_type_id = models.ForeignKey(ArtisteType, blank = True, null=True, on_delete=models.CASCADE)
    show_id = models.ForeignKey(Show, blank=True, null=True, on_delete=models.CASCADE)

class Representation(models.Model):
    show_id = models.ForeignKey(Show, blank=True, null=True, on_delete=models.CASCADE)
    when = models.DateTimeField()
    location_id = models.ForeignKey(Location, blank=True, null=True, on_delete=models.SET_NULL)

class User(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=255)
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    langue = models.CharField(max_length=2)

    def __str__(self):
        return self.login

class RepresentationUser(models.Model):
    representation_id = models.ForeignKey(Representation, blank=True, null=True, on_delete=models.DO_NOTHING)
    user_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING)
    places = models.IntegerField()








class Role(models.Model):
    role = models.CharField(max_length=30)

class RoleUser(models.Model):
    role_id = models.ForeignKey(Role, blank=True, null=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
