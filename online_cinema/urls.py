from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('reviews/', include('reviews.urls')),
    path('collections/', include('film_collections.urls')),
]