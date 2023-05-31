from django.db import models
from django.contrib.auth.models import User

class Locality(models.Model):
    postal_code = models.IntegerField(max_length=6)
    locality = models.CharField(max_length=60)
    
    def __str__(self):
        return self.locality


class Location(models.Model):
    slug = models.CharField(max_length=60, unique=True)
    designation = models.CharField(max_length=60)
    address = models.CharField(max_length=255)
    locality_id = models.ForeignKey(Locality, blank=True, null=True, on_delete=models.SET_NULL, related_name='locations')
    website = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.designation


class Show(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=60, blank=True, null=True)
    title = models.CharField('Show Title', max_length=255, blank=True, null=True)
    description = models.TextField('Show Description', blank=True, null=True)
    poster_url = models.CharField('Show Image', max_length=255, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    location_id = models.ForeignKey(Location, blank=True, null=True, on_delete=models.SET_NULL)
    bookable = models.BooleanField(blank=True, null=True)
    price = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    representations = models.ManyToManyField('Representation', blank=True)
    
    def get_representations(self):
        return self.representations.all()

    def __str__(self):
        return self.title
    
    def get_display_price(self):
        return "{0:.2f}".format(self.price)


class Type(models.Model):
    type = models.CharField(max_length=60)

    def __str__(self):
        return self.type


class Artist(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    types = models.ManyToManyField(Type, through='ArtisteType')

    def __str__(self):
        return f'{self.firstname} {self.lastname}'



class ArtisteType(models.Model):
    artist_id = models.ForeignKey(Artist, blank=True, null=True, on_delete=models.CASCADE)
    type_id = models.ForeignKey(Type, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "artist_type"
        
    def __str__(self):
        artist_str = str(self.artist_id) if self.artist_id else ''
        type_str = str(self.type_id) if self.type_id else ''
        return artist_str + ' ' + type_str



class ArtistTypeShow(models.Model):
    artiste_type_id = models.ForeignKey(ArtisteType, blank=True, null=True, on_delete=models.CASCADE)
    show_id = models.ForeignKey(Show, blank=True, null=True, on_delete=models.CASCADE)


class Representation(models.Model):
    show_id = models.ForeignKey(Show, blank=True, null=True, on_delete=models.CASCADE)
    when = models.DateTimeField(blank=True, null=True)
    location_id = models.ForeignKey(Location, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.show_id} - {self.when} - {self.location_id}"




class RepresentationUser(models.Model):
    representation_id = models.ForeignKey(Representation, blank=True, null=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING)
    places = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.representation_id} - {self.user_id} - {self.places}"
    
    def get_total_price(self):
        return self.places * self.representation_id.show_id.price



class Role(models.Model):
    role = models.CharField(max_length=30)

    def __str__(self):
        return self.role


class RoleUser(models.Model):
    role_id = models.ForeignKey(Role, blank=True, null=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
