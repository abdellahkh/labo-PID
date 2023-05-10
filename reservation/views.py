from django.shortcuts import render
from .forms import ShowRegistration
from .models import Show

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    shows = Show.objects.all()
    return render(request,'main/home.html', {'shows': shows})

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
            li = fm.cleaned_data['locality_id']
            bk = fm.cleaned_data['bookable']
            pr = fm.cleaned_data['price']
            reg = Show(slug = sl, title = ti, description = des, poster_url = pu, locality_id = li, bookable = bk, price = pr)
            reg.save()
            fm = ShowRegistration()
    else: 
        fm = ShowRegistration()
    return render(request, 'show/addandshow.html', {'form': fm})