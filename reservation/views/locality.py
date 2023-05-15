from django.http import Http404
from django.shortcuts import render

from reservation.models import Artist, Locality


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
