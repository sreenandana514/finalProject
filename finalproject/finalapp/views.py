from django.shortcuts import render, get_object_or_404,redirect
from django.shortcuts import HttpResponse
from .models import Category, Movie
from django.core.paginator import EmptyPage, InvalidPage, Paginator


def allMovieCat(request, c_slug=None):
    c_page = None
    movies_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        movies_list = Movie.objects.all().filter(category=c_page, available=True)
    else:
        movies_list = Movie.objects.all().filter(available=True)
    paginator = Paginator(movies_list, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        movies = paginator.page(page)
    except (EmptyPage, InvalidPage):
        movies = paginator.page(paginator.num_pages)

    return render(request, 'category.html', {'category': c_page, 'movies': movies})


def movieDetail(request, c_slug, movie_slug):
    try:
        movie = Movie.objects.get(category__slug=c_slug, slug=movie_slug)
    except Exception as e:
        raise e
    return render(request, 'movie.html', {'movie': movie})


