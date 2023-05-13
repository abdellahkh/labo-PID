from calendar import HTMLCalendar
import calendar
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ArtistDeleteForm, ShowRegistration, ArtistFormCreation
from .models import *
from datetime import datetime
from django.contrib import messages

# Import pagination Stuff
from django.core.paginator import Paginator 

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create your views here.
#def home(request):
#    shows = Show.objects.all()
#    return render(request,'main/home.html', {'shows': shows})

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    shows = Show.objects.all()

    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    
    cal = HTMLCalendar().formatmonth( year, month_number)
    now = datetime.now()
    current_year = now.year
    current_month = now.month

    return render(request,'main/home.html', {'shows': shows, 'year': year, 'month':month, 'month_number ': month_number, 'cal': cal, 'current_year': current_year, 'current_month': current_month})



def login(request):
    return render(request,'registration/login.html')

def register(request):
    return render(request,'registration/register.html')

def addandshow(request):
    if request.method == 'POST':
        fm = ShowRegistration(request.POST)
        if fm.is_valid():
            sl = fm.cleaned_data['slug']
            ti = fm.cleaned_data['title']
            des = fm.cleaned_data['description']
            pu = fm.cleaned_data['poster_url']
            li = fm.cleaned_data['location_id']
            bk = fm.cleaned_data['bookable']
            pr = fm.cleaned_data['price']
            reg = Show(slug = sl, title = ti, description = des, poster_url = pu, location_id = li, bookable = bk, price = pr)
            reg.save()
            fm = ShowRegistration()
    else: 
        fm = ShowRegistration()
    return render(request, 'show/addandshow.html', {'form': fm})


def allShows(request):
    #shows = Show.objects.all().order_by('?')
    shows_list = Show.objects.all()

    # Set up Pagination
    p = Paginator(Show.objects.all(), 3)
    page = request.GET.get('page')
    show = p.get_page(page)

    return render (request, "show/allShows.html", {'show_list': shows_list,"shows": show})
    
    
def allArtists(request):
    artists = Artist.objects.all()
    return render(request, "artist/allArtists.html", {'artists': artists})

def showArtist(request, artist_id):
    try:
        artist = Artist.objects.get(id=artist_id)
    except Artist.DoesNotExist:
        raise Http404('Artiste inexistant')
    
    title = 'Fiche artiste'

    return render(request, 'artist/showArtist.html', {'artist' : artist, 'title' : title})

def artistCreate(request):
    if request.method == 'POST':
        form = ArtistFormCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allArtists')
    else:
        form = ArtistFormCreation()

    title = "Creer un artiste"

    return render(request, 'artist/createArtist.html', {'form': form, 'title': title})



def editArtist(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)

    if request.method == 'POST':
        form = ArtistFormCreation(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            messages.success(request, ("Artiste a bien ete modifier"))
            return redirect('showArtist', artist_id=artist.id)
    else:
        form = ArtistFormCreation(instance=artist)

    title = 'Modifier un artiste'

    return render(request, 'artist/editArtist.html', {
        'artist': artist,
        'form': form,
        'title': title
    })

def deleteArtist(request, artist_id):
    try:
        artist = Artist.objects.get(id=artist_id)
    except Artist.DoesNotExist:
        raise Http404('Artist inexistant')

    if request.method == 'POST':
        form = ArtistDeleteForm(request.POST, instance=artist)
        if form.is_valid():
            artist.delete()
            messages.success(request, ("Artiste a bien ete supprimer"))
            return redirect('allArtists')
    else:
        form = ArtistDeleteForm(instance=artist)

    title = 'Supprimer un artiste'

    return render(request, 'artist/deleteArtist.html', {
        'artist': artist,
        'form': form,
        'title': title
    })