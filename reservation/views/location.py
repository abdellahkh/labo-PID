from django.shortcuts import render
from django.http import Http404
 
from reservation.models import Location

from calendar import HTMLCalendar
import calendar
import json
from django.conf import settings
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from os.path import join
from ..forms import ArtistDeleteForm, ShowRegistration, ArtistFormCreation, LocalityFormCreation
from ..models import *
from datetime import datetime
from django.contrib import messages
import os

# Import pagination Stuff
from django.core.paginator import Paginator

import logging

locality = models.ForeignKey(Locality, on_delete=models.SET_NULL , null=True, related_name='location')

 
def localityCreate(request):
    if request.method == 'POST':
        form = LocalityFormCreation(request.POST)
        if form.is_valid():
            locality = form.save()

            # Load existing data
            filepath = join(settings.BASE_DIR, 'reservation', 'fixtures', 'LocalityFixtures.json')
            if os.path.exists(filepath):
                with open(filepath, 'r') as f:
                    data = json.load(f)
            else:
                data = []

            # Add new locality
            data.append({
                "model": "reservation.locality",
                "pk": locality.pk,
                "fields": {
                    "postal_code": locality.postal_code,  # Assuming you have a postal_code field in your form
                    "locality": locality.locality,
                }
            })

            # Save data back to file
            with open(filepath, 'w') as f:
                json.dump(data, f)

            return redirect('allLocalities')
    else:
        form = LocalityFormCreation()
    title = "Créer une localité"
    return render(request, 'locality/createLocality.html', {'form': form, 'title': title})
