from django.contrib import admin
from .models import Collection

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description', 'owner__username')
    readonly_fields = ('created_at', 'updated_at')