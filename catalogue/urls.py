"""reservations.catalogue URL Configuration
"""
from django.urls import path
from . import views
app_name='catalogue'

urlpatterns = [
 path('artist/', views.artist.index, name='artist-index'),
 path('artist/<int:artist_id>', views.artist.show, name='artist-show'),
 #path('artist/edit/<int:artist_id>', views.artist.edit, name='artist-edit'),
 #path('artist/update/<int:artist_id>', views.artist.update, name='artist-update'),
 path('type/', views.type.index, name='type_index'),
 path('type/<int:type_id>', views.type.show, name='type_show'),
]