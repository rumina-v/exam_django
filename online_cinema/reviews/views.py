from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from movies.models import Movie
from .models import Review
from .forms import ReviewForm

class AddReviewView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/add_review.html'

    def form_valid(self, form):
        movie = get_object_or_404(Movie, id=self.kwargs['movie_id'])
        form.instance.movie = movie
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('movies:detail_movie', kwargs={'pk': self.kwargs['movie_id']})

class MovieReviewsView(ListView):
    model = Review
    template_name = 'reviews/movie_reviews.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return Review.objects.filter(movie_id=movie_id).select_related('user').order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie'] = get_object_or_404(Movie, id=self.kwargs['movie_id'])
        return context