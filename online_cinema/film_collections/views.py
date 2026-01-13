from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Collection
from .forms import CollectionForm

class CollectionListView(LoginRequiredMixin, ListView):
    model = Collection
    template_name = 'film_collections/collection_list.html'
    context_object_name = 'collections'
    paginate_by = 6

    def get_queryset(self):
        return Collection.objects.filter(owner=self.request.user)

class CollectionCreateView(LoginRequiredMixin, CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'film_collections/collection_form.html'
    success_url = reverse_lazy('collections:collection_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class CollectionUpdateView(LoginRequiredMixin, UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'film_collections/collection_form.html'
    success_url = reverse_lazy('collections:collection_list')

    def get_queryset(self):
        return Collection.objects.filter(owner=self.request.user)

class CollectionDeleteView(LoginRequiredMixin, DeleteView):
    model = Collection
    template_name = 'film_collections/collection_confirm_delete.html'
    success_url = reverse_lazy('collections:collection_list')

    def get_queryset(self):
        return Collection.objects.filter(owner=self.request.user)