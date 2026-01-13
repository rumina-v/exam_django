from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Collection
from .forms import CollectionForm

@login_required
def list_collections(request):
    collections = Collection.objects.filter(owner=request.user)
    return render(request, 'film_collections/list_collections.html', {'collections': collections})

@login_required
def create_collection(request):
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.owner = request.user
            collection.save()
            form.save_m2m()  # сохраняем связи ManyToMany
            return redirect('collections:list_collections')
    else:
        form = CollectionForm()
    return render(request, 'film_collections/create_collection.html', {'form': form})

@login_required
def edit_collection(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id, owner=request.user)
    if request.method == 'POST':
        form = CollectionForm(request.POST, instance=collection)
        if form.is_valid():
            form.save()
            return redirect('collections:list_collections')
    else:
        form = CollectionForm(instance=collection)
    return render(request, 'film_collections/edit_collection.html', {'form': form, 'collection': collection})

@login_required
def delete_collection(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id, owner=request.user)
    if request.method == 'POST':
        collection.delete()
        return redirect('collections:list_collections')
    return render(request, 'film_collections/delete_collection.html', {'collection': collection})