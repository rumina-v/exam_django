from django.urls import path
from . import views

app_name = 'collections'

urlpatterns = [
    path('', views.CollectionListView.as_view(), name='collection_list'),
    path('create/', views.CollectionCreateView.as_view(), name='collection_create'),
    path('edit/<int:pk>/', views.CollectionUpdateView.as_view(), name='collection_update'),
    path('delete/<int:pk>/', views.CollectionDeleteView.as_view(), name='collection_delete'),
]