from django.shortcuts import render, redirect, reverse
from .forms import UserSignupForm
from .models import CustomUser

def signup(request):
    # blank instance of UserCreationForm
    form = UserSignupForm()
    
    if request.method == 'POST':

        # create a form with the form data from the request
        form = UserSignupForm(request.POST)    

        # validate the form
        if form.is_valid():
            form.save()

            # if the form is saved, redirect to the user list template
            return redirect(reverse('login'))

    # pass to template
    context = {
        'form':form
    }

    return render(request, 'signup.html', context)

def users_list(request):

    users = CustomUser.objects.all()

    context = {
        'users': users
    }
    
    return render(request, 'user-list.html', context) 

def profile(request, id):

    return(request, 'profile.html')
