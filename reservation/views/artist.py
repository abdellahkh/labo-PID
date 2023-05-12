from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib import messages

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