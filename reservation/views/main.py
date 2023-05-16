
import logging
from datetime import datetime
from calendar import HTMLCalendar
import calendar
from django.shortcuts import render

from reservation.models import Show
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

def displayUserAccount(request):
    return render(request, 'registration/register.html')