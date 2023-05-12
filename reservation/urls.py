
from django import views
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home, name="home"),
    path('addandshow',addandshow, name="addandshow"),
    path('<int:year>/<str:month>/',home, name="home"),
    path('all_shows', allShows , name="allShows"),
    path('artist', allArtists , name="allArtists"),   # Visuel a faire
    path('artist/<int:artist_id>',showArtist, name='showArtist'),  # a rendre plus jolie
    path('artist/create/', artistCreate, name='artistCreate'),  # a rendre plus jolie
    path('artist/<int:artist_id>/edit/', editArtist , name='artist_edit'), # a rendre plus jolie


    
    #path('artist/<int:artist_id>/delete', views.artist.delete, name='artist_delete'),
    #path('type/', views.type.index, name='type_index'),
    #path('type/<int:type_id>', views.type.show, name='type_show'),
    #path('locality/', views.locality.index, name='locality_index'),
    #path('locality/<int:locality_id>', views.locality.show, name='locality_show'),
    #path('role/', views.role.index, name='role_index'),
    #path('role/<int:role_id>', views.role.show, name='role_show'),
    #path('location/', views.location.index, name='location_index'),
    #path('location/<int:location_id>', views.location.show, name='location_show'),
    #path('show/', views.show_detail.index, name='show_index'),
    #path('show/<int:show_id>', views.show_detail.show, name='show_show'),
    #path('representation/', views.representation.index, name='representation_index'),
    #path('representation/<int:representation_id>', views.representation.show, name='representation_show'),


]
