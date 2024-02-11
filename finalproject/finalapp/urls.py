from django.urls import path
from . import views

app_name = 'finalapp'
urlpatterns = [
    path('', views.allMovieCat, name='allMovieCat'),
    path('<slug:c_slug>/', views.allMovieCat, name='movies_by_category'),
    path('<slug:c_slug>/<slug:movie_slug>/', views.movieDetail, name='moviesCatdetail'),
]
