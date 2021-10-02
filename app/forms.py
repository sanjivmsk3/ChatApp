from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from app.models import PostDetails


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2')

class PostForm(forms.ModelForm):
    class Meta:
        model = PostDetails
        fields = ('title','image','description')