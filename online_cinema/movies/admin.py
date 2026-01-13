from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'year', 'owner', 'created_at')
    list_filter = ('year', 'genre', 'owner')
    search_fields = ('title', 'director', 'genre')
    readonly_fields = ('created_at', 'updated_at')