from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('movie/<int:movie_id>/add/', views.add_review, name='add_review'),
    path('movie/<int:movie_id>/', views.movie_reviews, name='movie_reviews'),
]