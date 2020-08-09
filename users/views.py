from django.shortcuts import render
from .forms import UserSignupForm

def signup(request):
    # blank instance of UserCreationForm
    form = UserSignupForm()
    
    if request.method == 'POST':

        # create a form with the form data from the request
        form = UserSignupForm(request.POST)    


        if form.is_valid():
            form.save()


    # pass to template
    context = {
        'form':form
    }

    return render(request, 'signup.html', context)

def user_list(request):
    return render(request, 'user-list.html') 

def profile(request, id):

    return(request, 'profile.html')
