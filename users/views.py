from django.shortcuts import render
from .forms import UserSignupForm

def signup(request):
    # blank instance of UserCreationForm
    form = UserSignupForm()

    # pass to template
    context = {
        'form':form
    }

    return render(request, 'signup.html', context)

def user_list(request):
    return render(request, 'user-list.html') 

def profile(request, id):

    return(request, 'profile.html')
