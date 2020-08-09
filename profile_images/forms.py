from django import forms

from .models import ProfileImage

class ProfileImageUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileImage
        fields = ['image']