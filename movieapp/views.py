from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from movieapp.forms import MovieForm
from movieapp.models import movie


def index(request):
    filim = movie.objects.all()
    context = {
        'movie_list': filim
    }
    return render(request, 'index.html', context)


def detail(request, movie_id):
    filim = movie.objects.get(id=movie_id)
    return render(request, 'detail.html', {'movie': filim})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        filim = movie(name=name, desc=desc, year=year, img=img)
        filim.save()
    return render(request, 'add.html')


def update(request, id):
    film = movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=film)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'update.html', {'form': form, 'filim': film})


def delete(request, id):
    if request.method == 'POST':
        film = movie.objects.get(id=id)
        film.delete()
        return redirect('/')
    return render(request, 'delete.html')
