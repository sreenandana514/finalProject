from django import forms
from .models import Profile
from finalapp.models import Movie, Category


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email']


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['title', 'desc', 'actors', 'trailer_link', 'poster', 'release_date', 'available']
