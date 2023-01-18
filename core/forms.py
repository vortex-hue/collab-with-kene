from django.contrib.auth.models import User

class LoginForm(froms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)