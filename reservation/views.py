from calendar import HTMLCalendar
import calendar
import json
from django.conf import settings
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from os.path import join
from .forms import ArtistDeleteForm, ShowRegistration, ArtistFormCreation, UpdateUserForm
from .models import *
from datetime import datetime
from django.contrib import messages

# Import pagination Stuff
from django.core.paginator import Paginator

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create your views here.
# def home(request):
#    shows = Show.objects.all()
#    return render(request,'main/home.html', {'shows': shows})


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    shows = Show.objects.all()

    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    cal = HTMLCalendar().formatmonth(year, month_number)
    now = datetime.now()
    current_year = now.year
    current_month = now.month

    return render(request, 'main/home.html', {'shows': shows, 'year': year, 'month': month, 'month_number ': month_number, 'cal': cal, 'current_year': current_year, 'current_month': current_month})


def login(request):
    return render(request, 'registration/login.html')


def register(request):
    return render(request, 'registration/register.html')


def addshow(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            fm = ShowRegistration(request.POST, request.FILES)
            if fm.is_valid():
                sl = fm.cleaned_data['slug']
                ti = fm.cleaned_data['title']
                des = fm.cleaned_data['description']
                pu = fm.cleaned_data['poster_url']
                li = fm.cleaned_data['location_id']
                bk = fm.cleaned_data['bookable']
                pr = fm.cleaned_data['price']
                im = fm.cleaned_data['image']
                reg = Show(slug=sl, title=ti, description=des,
                        poster_url=pu, location_id=li, bookable=bk, price=pr, image=im)
                reg.save()
                fm = ShowRegistration()
                messages.success(request, ("Sauvegarde reussi"))
        else:
            fm = ShowRegistration()
    else:
        messages.success(request, ("Vous n'avez pas les droits"))
        return redirect('home')
    locations = Location.objects.all()
    return render(request, 'show/addshow.html', {'form': fm, 'locs': locations})


def allShows(request):
    # shows = Show.objects.all().order_by('?')
    shows_list = Show.objects.all()

    # Set up Pagination
    p = Paginator(Show.objects.all(), 3)
    page = request.GET.get('page')
    show = p.get_page(page)

    return render(request, "show/allShows.html", {'show_list': shows_list, "shows": show})

def search_shows(request):
    if request.method == "POST":
        searched = request.POST['searched']
        showsResults = Show.objects.filter(title__contains=searched)
        return render(request, "search_shows.html", {'searched': searched, 'showsResults' : showsResults})
    else: 
        return render(request, "search_shows.html",{})

    

def editShow(request, show_id):
    if request.user.is_superuser:
        show = get_object_or_404(Show, id=show_id)

        if request.method == 'POST':
            form = ShowRegistration(request.POST, instance=show)
            if form.is_valid():
                form.save()
                messages.success(request, ("Artiste a bien ete modifier"))
                return redirect('show_detail', show_id=show.id)
        else:
            form = ShowRegistration(instance=show)

        title = 'Modifier un show'
    else:
        messages.success(request, ("Vous n'avez pas les droits"))
        return redirect('home')

    return render(request, 'show/updateShow.html', {
        'show': show,
        'form': form,
        'title': title
    })


def allArtists(request):
    artists = Artist.objects.all()
    return render(request, "artist/allArtists.html", {'artists': artists})


def displayShow(request, show_id):
    try:
        show = Show.objects.get(id=show_id)
    except Show.DoesNotExist:
        raise Http404('Pas de show identifier')

    title = 'Fiche d\'un show'
    return render(request, "show/show.html", {'show': show, 'title': title})


def showArtist(request, artist_id):
    try:
        artist = Artist.objects.get(id=artist_id)
    except Artist.DoesNotExist:
        raise Http404('Artiste inexistant')

    title = 'Fiche artiste'

    return render(request, 'artist/showArtist.html', {'artist': artist, 'title': title})


def artistCreate(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ArtistFormCreation(request.POST)
            if form.is_valid():
                artist = form.save()
                # Load existing data
                with open(join(settings.BASE_DIR, 'reservation', 'fixtures', 'ArtistFixtures.json'), 'r') as f:
                    data = json.load(f)
                # Add new artist
                data.append({
                    "model": "reservation.artist",
                    "pk": artist.pk,
                    "fields": {
                        "firstname": artist.firstname,
                        "lastname": artist.lastname,
                    }
                })
                # Save data back to file
                with open(join(settings.BASE_DIR, 'reservation', 'fixtures', 'ArtistFixtures.json'), 'w') as f:
                    json.dump(data, f)
                return redirect('allArtists')
        else:
            form = ArtistFormCreation()
        title = "Creer un artiste"
    else:
        messages.success(request, ("Vous n'avez pas les droits"))
        return redirect('home')
    return render(request, 'artist/createArtist.html', {'form': form, 'title': title})


def editArtist(request, artist_id):
    if request.user.is_superuser:
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
    else:
        messages.success(request, ("Vous n'avez pas les droits"))
        return redirect('home')
    return render(request, 'artist/editArtist.html', {
        'artist': artist,
        'form': form,
        'title': title
    })


def deleteArtist(request, artist_id):
    if request.user.is_superuser:
        try:
            artist = Artist.objects.get(id=artist_id)
        except Artist.DoesNotExist:
            raise Http404('Artist inexistant')

        if request.method == 'POST':
            form = ArtistDeleteForm(request.POST, instance=artist)
            if form.is_valid():
                # Load existing data
                with open(join(settings.BASE_DIR, 'reservation', 'fixtures', 'ArtistFixtures.json'), 'r') as f:
                    data = json.load(f)

                # Filter out the deleted artist
                data = [item for item in data if item["pk"] != artist_id]

                # Save the data back to the file
                with open(join(settings.BASE_DIR, 'reservation', 'fixtures', 'ArtistFixtures.json'), 'w') as f:
                    json.dump(data, f, indent=2)

                artist.delete()
                messages.success(request, ("Artiste a bien ete supprimer"))
                return redirect('allArtists')
        else:
            form = ArtistDeleteForm(instance=artist)

        title = 'Supprimer un artiste'
    else:
        messages.success(request, ("Vous n'avez pas les droits"))
        return redirect('home')
    return render(request, 'artist/deleteArtist.html', {
        'artist': artist,
        'form': form,
        'title': title
    })


# Create your views here.
def show_all_type(request):
    types = Type.objects.all()

    title = 'Liste des types'

    return render(request, 'type/showType.html', {
        'types': types,
        'title': title
    })


def showType(request, type_id):
    try:
        type = Type.objects.get(id=type_id)
    except Type.DoesNotExist:
        raise Http404('Type inexistant')

    title = 'Fiche d\'un type'

    return render(request, 'type/showType.html', {
        'type': type,
        'title': title
    })


def allLocality(request):
    localities = Locality.objects.all()
    return render(request, "localities/localities.html", {'localities': localities})


def showLocality(request, locality_id):
    try:
        locality = Locality.objects.get(id=locality_id)
    except Artist.DoesNotExist:
        raise Http404('La locqalite n\'existe pas')

    title = 'Fiche localite'

    return render(request, 'localities/localities.html', {'locality': locality, 'title': title})




def displayUserAccount(request):
    from django.contrib.auth.models import User
    
    user = get_object_or_404(User, id=request.user.id)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, ("Modification reussi"))
            return redirect('home')
        else:
            messages.success(request, ("form invalid"))
    else:
        form = UpdateUserForm(instance=user)

    title = 'Modifier son profil'

    return render(request, 'registration/myaccount.html', {
        'show': user,
        'form': form,
        'title': title
    })
