from django import forms
from .models import Post, Comment, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('text','image')

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


#Change profile

# class EditProfileForm(UserChangeForm):
#
#     class Meta:
#         model = UserProfile
#         fields = ['image','phone','city','description']



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image','phone','description','city']