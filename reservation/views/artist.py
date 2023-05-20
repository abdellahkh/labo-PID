from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib import messages
import json
from django.conf import settings
from os.path import join

from reservation.models import Artist
from reservation.forms import ArtistDeleteForm, ArtistFormCreation

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

    return render(request, 'artist/deleteArtist.html', {
        'artist': artist,
        'form': form,
        'title': title
    })