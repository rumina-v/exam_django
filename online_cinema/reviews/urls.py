from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('movie/<int:movie_id>/add/', views.AddReviewView.as_view(), name='add_review'),
    path('movie/<int:movie_id>/', views.MovieReviewsView.as_view(), name='movie_reviews'),
]