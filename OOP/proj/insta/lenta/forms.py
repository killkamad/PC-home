from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text','image')

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


#Change profile

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['email','first_name','last_name','password']



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)