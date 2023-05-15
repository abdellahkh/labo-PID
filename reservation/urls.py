from django.urls import path
from . import views
from reservation.views.main import *
from reservation.views.show import *
from reservation.views.artist import *
from reservation.views.type import *
from reservation.views.locality import *
app_name='reservation'

urlpatterns = [


    path('', views.main.home , name="home"),

    path('addshow', views.show.addshow, name="addshow"),
    path('all_shows', views.show.allShows , name="allShows"),
    path('show/<int:show_id>', views.show.displayShow , name="show_detail" ),
    path('show/<int:show_id>/edit', views.show.editShow, name="editShow"),
    
    path('artist', views.artist.allArtists , name="allArtists"),   # Visuel a faire
    path('artist/<int:artist_id>',views.artist.showArtist, name='showArtist'),  # a rendre plus jolie
    path('artist/create/', views.artist.artistCreate, name='artistCreate'),  # a rendre plus jolie
    path('artist/<int:artist_id>/edit/', views.artist.editArtist , name='artist_edit'), # a rendre plus jolie
    path('artist/<int:artist_id>/delete', views.artist.deleteArtist, name='deleteArtist'),  # a rendre plus jolie
    
    path('type/',  views.type.show_all_type , name='type_show'),
    path('type/<int:type_id>', views.type.showType, name='type_detail'),

    path('locality/', views.locality.allLocality, name='locality_index'),
    path('locality/<int:locality_id>', views.locality.showLocality, name='locality_show'),


    #path('role/', views.role.index, name='role_index'),
    #path('role/<int:role_id>', views.role.show, name='role_show'),
    #path('location/', views.location.index, name='location_index'),
    #path('location/<int:location_id>', views.location.show, name='location_show'),
    #path('show/', views.show_detail.index, name='show_index'),
    #path('show/<int:show_id>', views.show_detail.show, name='show_show'),
    #path('representation/', views.representation.index, name='representation_index'),
    #path('representation/<int:representation_id>', views.representation.show, name='representation_show'),


]
