from django.shortcuts import render
from django.db.models import Q
from finalapp.models import Movie


def SearchResult(request):
    movies = None
    query = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        movies = Movie.objects.all().filter(Q(title__contains=query) | Q(desc__contains=query))

    return render(request, 'search.html', {'query': query, 'movies': movies})
