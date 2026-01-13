from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.list_movies, name='list_movies'),
    path('add/', views.add_movie, name='add_movie'),
    path('<int:movie_id>/', views.detail_movie, name='detail_movie'),
]