from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from movies.models import Movie
from .models import Review
from .forms import ReviewForm

@login_required
def add_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            return redirect('movies:detail_movie', movie_id=movie.id)
    else:
        form = ReviewForm()
    return render(request, 'reviews/add_review.html', {'form': form, 'movie': movie})

def movie_reviews(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = Review.objects.filter(movie=movie).select_related('user').order_by('-created_at')
    return render(request, 'reviews/movie_reviews.html', {'movie': movie, 'reviews': reviews})