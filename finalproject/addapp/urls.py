from django.urls import path
from . import views

app_name = 'addapp'
urlpatterns = [
    path('add', views.add_movie, name='add_movie'),
    path('add/view_profile', views.view_profile, name='view_profile'),
    path('add/edit_profile', views.edit_profile, name='edit_profile'),
    path('exit/', views.exit_profile, name='exit_profile'),
    path('movie/<slug:slug>/edit/edit_movie', views.edit_movie, name='edit_movie'),
    path('movies/<slug:slug>/delete/', views.delete_movie, name='delete_movie'),

]
