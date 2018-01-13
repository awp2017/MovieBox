from django import forms
from MovieBox.models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'date', 'genre', 'actors')

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
