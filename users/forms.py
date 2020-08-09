from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

# extend UserCreationForm
class UserSignupForm(UserCreationForm):
    class Meta:
        # the model on which to base the form
        model = CustomUser

        # these fields will show up when the form is rendered
        fields = ['username', 'password1', 'password2']
