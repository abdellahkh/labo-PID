from django.contrib import admin
from .models import Show
from .models import Location
from .models import Locality
from .models import Artist
from .models import Type
from .models import ArtisteType
from .models import ArtistTypeShow
from .models import Representation
from .models import User
from .models import RepresentationUser
from .models import Role
from .models import RoleUser


# Register your models here.
@admin.register(Show)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'title', 'description', 'poster_url', 'location_id', 'bookable', 'price', 'created_at')

admin.site.register(Location)
admin.site.register(Locality)
admin.site.register(Artist)
admin.site.register(Type)
admin.site.register(ArtisteType)
admin.site.register(ArtistTypeShow)
admin.site.register(Representation)
admin.site.register(User)
admin.site.register(RepresentationUser)
admin.site.register(Role)
admin.site.register(RoleUser)
  