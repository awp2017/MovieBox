from django import forms
from MovieBox.models import Movie
from MovieBox.models import Actor, MBUserProfile
from django.contrib.auth.models import User

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'date', 'genre', 'actors', 'description', 'cover')

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ('first_name', 'last_name', 'birth_date', 'picture')

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class SignUpForm(forms.ModelForm):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MBUserProfile
        fields = [
            'first_name', 'last_name', 'birth_date',
            'profile_pic'
        ]

    def save(self, commit=True):
        instance = super(SignUpForm, self).save(commit=False)
        user = User(username=self.data['email'], password=self.data['password'])
        user.save()
        instance.user = user
        instance.save()
        return instance
