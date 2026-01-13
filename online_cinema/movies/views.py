from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Movie

class MovieListView(LoginRequiredMixin, ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        director = self.request.GET.get('director')
        genre = self.request.GET.get('genre')
        year = self.request.GET.get('year')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if director:
            queryset = queryset.filter(director__icontains=director)
        if genre:
            queryset = queryset.filter(genre__icontains=genre)
        if year:
            queryset = queryset.filter(year=year)

        return queryset

class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    template_name = 'movies/movie_form.html'
    fields = ['title', 'director', 'genre', 'description', 'year', 'poster']
    success_url = reverse_lazy('movies:movie_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    template_name = 'movies/movie_form.html'
    fields = ['title', 'director', 'genre', 'description', 'year', 'poster']
    success_url = reverse_lazy('movies:movie_list')

    def get_queryset(self):
        return Movie.objects.filter(owner=self.request.user)

class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = 'movies/movie_confirm_delete.html'
    success_url = reverse_lazy('movies:movie_list')

    def get_queryset(self):
        return Movie.objects.filter(owner=self.request.user)