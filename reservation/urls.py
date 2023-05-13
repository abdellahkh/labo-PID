
from django import views
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home, name="home"),
    path('addandshow',addandshow, name="addandshow"),
    path('<int:year>/<str:month>/',home, name="home"),
    path('all_shows', allShows , name="allShows"),
    path('all_artists', allArtists , name="allArtists"),
]
