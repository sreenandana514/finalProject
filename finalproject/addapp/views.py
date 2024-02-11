from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.utils.text import slugify

from django.shortcuts import render, get_object_or_404, redirect
from .forms import MovieForm
from finalapp.models import Movie

from finalapp.models import Category, Movie
from .models import Profile
from .forms import ProfileForm, MovieForm

from django.shortcuts import render, redirect, get_object_or_404
from finalapp.models import Category, Movie

from django.shortcuts import render, get_object_or_404, redirect


def add_movie(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title', '')
        slug = slugify(title)
        desc = request.POST.get('desc', '')
        poster = request.FILES.get('poster', '')  # Use get() to avoid KeyError
        release_date = request.POST.get('release_date', '')
        actors = request.POST.get('actors', '')
        trailer_link = request.POST.get('trailer_link', '')
        available = request.POST.get('available') == 'on'
        category_name = request.POST.get('category', '')
        try:
            category = Category.objects.get(name=category_name)
            movie = Movie(title=title, slug=slug, desc=desc, category=category, poster=poster,
                          release_date=release_date, actors=actors, trailer_link=trailer_link, available=available)
            movie.user = request.user
            movie.save()
            return redirect('finalapp:allMovieCat')  # Redirect after successful form submission
        except Category.DoesNotExist:
            # Handle the case where the category does not exist
            error_message = f"The category '{category_name}' does not exist."
            return render(request, 'add_movie.html', {'categories': categories, 'error_message': error_message})

    return render(request, 'add_movie.html', {'categories': categories})


def view_profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'view_profile.html', {'profile': profile})


def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('addapp:view_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})


def exit_profile(request):
    # Redirect the user to the homepage or any other desired page
    return redirect('finalapp:allMovieCat')  # Replace 'home' with the desired URL name


def edit_movie(request, slug):
    movie = Movie.objects.get(slug=slug, user=request.user)
    if request.method == 'POST':
        form = MovieForm(request.POST,request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('finalapp:allMovieCat')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'edit_movie.html', {'form': form, 'movie':movie})


def delete_movie(request, slug):
    movie = get_object_or_404(Movie, slug=slug, user=request.user)
    # Your delete logic here
    movie.delete()
    return redirect('finalapp:allMovieCat')
