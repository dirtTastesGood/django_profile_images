from django.shortcuts import render, redirect, reverse

from .models import CustomUser
from .forms import UserSignupForm

from profile_images.models import ProfileImage
from profile_images.forms import ProfileImageUpdateForm

def signup(request):
    # blank instance of UserCreationForm
    form = UserSignupForm()
    
    if request.method == 'POST':

        # create a form with the form data from the request
        form = UserSignupForm(request.POST)    

        # validate the form
        if form.is_valid():

            # create a model object but don't save it yet
            new_user = form.save(commit=False)

            # create a new profile image object
            profile_image = ProfileImage.objects.create()

            # associate the profile image to the new user
            new_user.profile_image = profile_image

            # save new CustomUser instance
            new_user.save()

            # if the form is saved, redirect to the login template
            return redirect(reverse('users:login'))

    context = {
        "form": form
    }

    return render(request, 'signup.html' ,context)


def users_list(request):

    users = CustomUser.objects.all()

    context = {
        'users': users
    }
    
    return render(request, 'user-list.html', context) 

def profile(request):

    image_form = ProfileImageUpdateForm(instance=request.user.profile_image)

    context = {
        'img_form': image_form,
    }

    return(render(request, 'profile.html', context))
