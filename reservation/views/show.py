from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from reservation.forms import ShowRegistration
from django.contrib import messages
from django.core.paginator import Paginator

from reservation.models import Show


def displayShow(request, show_id):
    try:
        show = Show.objects.get(id=show_id)
    except Show.DoesNotExist:
        raise Http404('Pas de show identifier')

    title = 'Fiche d\'un show'
    return render(request, "show/show.html", {'show': show, 'title': title})

def addshow(request):
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
            reg = Show(slug=sl, title=ti, description=des,
                       poster_url=pu, location_id=li, bookable=bk, price=pr)
            if 'image' in request.FILES:
                reg.image = request.FILES['image']
            reg.save()
            fm = ShowRegistration()
    else:
        fm = ShowRegistration()
    return render(request, 'show/addshow.html', {'form': fm})




def editShow(request, show_id):
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

    return render(request, 'show/updateShow.html', {
        'show': show,
        'form': form,
        'title': title
    })

def allShows(request):
    # shows = Show.objects.all().order_by('?')
    shows_list = Show.objects.all()

    # Set up Pagination
    p = Paginator(Show.objects.all(), 3)
    page = request.GET.get('page')
    show = p.get_page(page)

    return render(request, "show/allShows.html", {'show_list': shows_list, "shows": show})
