from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.MovieListView.as_view(), name='movie_list'),
    path('add/', views.MovieCreateView.as_view(), name='movie_create'),
    path('edit/<int:pk>/', views.MovieUpdateView.as_view(), name='movie_update'),
    path('delete/<int:pk>/', views.MovieDeleteView.as_view(), name='movie_delete'),
]