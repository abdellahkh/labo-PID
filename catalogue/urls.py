"""reservations.catalogue URL Configuration
"""
from django.urls import path
from . import views
app_name='catalogue'
urlpatterns = [
 path('artist/', views.artist.index, name='artist-index'),
 path('artist/<int:artist_id>', views.artist.show, name='artist-show'),
]