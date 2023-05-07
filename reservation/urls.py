
from django import views
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home, name="home"),
]
