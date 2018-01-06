from django import forms
from MovieBox.models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'year', 'genre', 'actors')