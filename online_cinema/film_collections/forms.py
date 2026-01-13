from django import forms
from .models import Collection
from movies.models import Movie

class CollectionForm(forms.ModelForm):
    movies = forms.ModelMultipleChoiceField(
        queryset=Movie.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Collection
        fields = ['name', 'description', 'movies']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }