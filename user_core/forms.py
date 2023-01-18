from django import forms
from .models import Profile



class FaceLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    class meta:
        model = Profile
        fields = ['username']
