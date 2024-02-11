from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from addapp.models import Profile


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    img = models.ImageField(upload_to='genre', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('finalapp:movies_by_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Movie(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    poster = models.ImageField(upload_to='poster', blank=True)
    release_date = models.DateTimeField()
    actors = models.TextField(max_length=500, blank=True)
    trailer_link = models.URLField(blank=True)
    available = models.BooleanField(default=True)
    user = models.ForeignKey(get_user_model() , on_delete=models.CASCADE, default=1)

    def get_url(self):
        return reverse('finalapp:moviesCatdetail', args=[self.category.slug, self.slug])

    class Meta:
        ordering = ('title',)
        verbose_name = 'movie'
        verbose_name_plural = 'movies'

    def __str__(self):
        return '{}'.format(self.title)
