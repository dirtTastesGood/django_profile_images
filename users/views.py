from django.shortcuts import render, redirect, reverse
from django.conf import settings

from .models import CustomUser
from .forms import UserSignupForm

from profile_images.models import ProfileImage
from profile_images.forms import ProfileImageUpdateForm

from pathlib import Path, PurePath
from PIL import Image

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
    
    # blank image form
    image_form = ProfileImageUpdateForm()

    # when the form is submitted
    if request.method == 'POST':
        # instance of form with data and files from request
        image_form = ProfileImageUpdateForm(
            data=request.POST, 
            files=request.FILES,
        )
        # if the form contains a file
        if request.FILES:
            # validate the form
            if image_form.is_valid():
                
                current_user = CustomUser.objects.get(username=request.user.username)
                # get the current user object
                print("HAS PROFILE IMAGE: ", current_user.has_profile_image())

                # delete current profile, if it exists
                if current_user.has_profile_image():
                    old_image = ProfileImage.objects.get(
                        id=current_user.profile_image_id
                    )

                    old_image_name = PurePath(old_image.image.name).name
                    
                    if old_image_name != 'default_profile_image.jpg':
                        old_image_path = Path(
                            settings.MEDIA_ROOT / 
                            old_image.image.name
                        )

                        Path.unlink(old_image_path, missing_ok=True)

                        old_image.delete()
                else:
                    print(f'{current_user} does not have a profile image')
                # create a model object but don't save it yet
                new_profile_image = image_form.save(commit=False)
                
                # associate the new image with the current user
                current_user.profile_image = new_profile_image

                # img_file = request.FILES.get("profile_image")
                # img_name = img_file.name
                img = Image.open(new_profile_image.image)

                print("IMG: ",img)
                # img_extension = img_name.split(".")[-1].lower()

                # if img_extension == 'jpeg':
                #     img_extension = 'jpg'

                # if img.height > 500 or img.width > 500:
                #     output_size = (500, 500)
                #     img.thumbnail(output_size)

                # change the current user's profile image to the new profile image
                request.user.profile_image = new_profile_image
                new_profile_image.customuser = current_user
                
                image_form.save()
                request.user.save()


    context = {
        'img_form': image_form,
    }

    return(render(request, 'profile.html', context))
