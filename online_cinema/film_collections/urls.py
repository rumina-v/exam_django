from django.urls import path
from . import views

app_name = 'collections'

urlpatterns = [
    path('', views.list_collections, name='list_collections'),
    path('create/', views.create_collection, name='create_collection'),
    path('edit/<int:collection_id>/', views.edit_collection, name='edit_collection'),
    path('delete/<int:collection_id>/', views.delete_collection, name='delete_collection'),
]