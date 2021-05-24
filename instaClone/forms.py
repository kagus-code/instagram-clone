from django import forms
from .models import Image,Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from instaClone import models


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')

class UploadImageForm(forms.ModelForm):
  class Meta:
    model = Image
    exclude = ['likes','pub_date','creator']

class PostCommentForm(forms.ModelForm):
  class Meta:
    model =  Comment

    exclude = ['image','pub_date','user']




