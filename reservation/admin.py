from django.contrib import admin
from .models import Show
# Register your models here.
@admin.register(Show)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'title', 'description', 'poster_url', 'locality_id', 'bookable', 'price')


  