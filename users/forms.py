from django import forms
from users.models import CustomUser, ProfileImage
from django.contrib.auth.forms import UserCreationForm, UserUpdateForm

class UserSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']

class ProfileImageUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileImage
        fields = ['image']