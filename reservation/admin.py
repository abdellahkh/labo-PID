from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
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
class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'slug', 'title', 'description', 'poster_url', 'location_id', 'bookable', 'price', 'created_at')

@admin.register(Location)
class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'slug', 'designation')


@admin.register(Locality)
class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'postal_code', 'locality')

@admin.register(Type)
class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'type')



@admin.register(ArtistTypeShow)
class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ()


admin.site.register(Artist)

admin.site.register(ArtisteType)

admin.site.register(Representation)
admin.site.register(User)
admin.site.register(RepresentationUser)
admin.site.register(Role)
admin.site.register(RoleUser)
  