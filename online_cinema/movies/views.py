from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Movie
from .forms import MovieForm

@login_required
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.owner = request.user
            movie.save()
            return redirect('movies:list_movies')
    else:
        form = MovieForm()
    return render(request, 'movies/add_movie.html', {'form': form})

def detail_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.reviews.all().select_related('user').order_by('-created_at')
    form = None
    if request.user.is_authenticated:
        form = ReviewForm()
    return render(request, 'movies/detail_movie.html', {
        'movie': movie,
        'reviews': reviews,
        'form': form
    })

def list_movies(request):
    movies = Movie.objects.all()

    # Фильтрация
    title = request.GET.get('title')
    director = request.GET.get('director')
    genre = request.GET.get('genre')
    year = request.GET.get('year')

    if title:
        movies = movies.filter(title__icontains=title)
    if director:
        movies = movies.filter(director__icontains=director)
    if genre:
        movies = movies.filter(genre__icontains=genre)
    if year:
        movies = movies.filter(year=year)

    return render(request, 'movies/list_movies.html', {'movies': movies})