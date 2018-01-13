from django import forms
from MovieBox.models import Movie
from MovieBox.models import Actor

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'date', 'genre', 'actors', 'description')

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ('first_name', 'last_name', 'birth_date', 'picture')

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
