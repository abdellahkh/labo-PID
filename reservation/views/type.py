from django.shortcuts import render
from django.http import Http404

from models import Type


# Create your views here.
def show_all_type(request):
    types = Type.objects.all()

    title = 'Liste des types'

    return render(request, 'type/index.html', {
        'types': types,
        'title': title
    })


def showType(request, type_id):
    try:
        type = Type.objects.get(id=type_id)
    except Type.DoesNotExist:
        raise Http404('Type inexistant')

    title = 'Fiche d\'un type'

    return render(request, 'type/show.html', {
        'type': type,
        'title': title
    })
