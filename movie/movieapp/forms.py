from .models import Movie
from django import forms

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name','desc','year','img']