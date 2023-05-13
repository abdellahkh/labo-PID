from calendar import HTMLCalendar
import calendar
from django.shortcuts import render
from .forms import ShowRegistration
from .models import *
from datetime import datetime

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
    shows = Show.objects.all()
    return render(request, "show/allShows.html", {'shows': shows})

def allArtists(request):
    artists = Artist.objects.all()
    return render(request, "artist/allArtists.html", {'artists': artists})