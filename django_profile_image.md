# Profile Images in Django

This guide will walk throught the steps necessary adding a `profile_image` to an instance of a user model. 

The project in this guide will be setup in a [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/) environment and all commands will be issed from within the environment unless otherwise noted. Commands will be executed on a Linux terminal.

## Project Setup

Create a directory for your project and navigate into it

    $ mkdir <PROJECT_NAME>
    $ cd <PROJECT_NAME>

Create the Pipenv environment

    $ pipenv shell

Install Django

    $ pipenv install django

Start a Django project

    $ django-admin startproject <PROJECT_NAME> .

The dot after `<PROJECT_NAME>` will tell Django to start the project in the current directory.

## Create Apps

Create `users` app

    $ python manage.py startapp users

Create `profile_images` app

    $ python manage.py startapp profile_images

In your project's `settings.py`, add `users` and `profile_images` to the list of installed apps.

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        ...
        ...
        ...
        'users',           # add this
        'profile_images',  # add this
    ]

## Setup Templates

We'll be using a project-level templates folder for all of our templates. App-level templates can be used with the proper path adjustments.

Point Django to your project-level `templates` directory

In `settings.py`

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'], # add this 

            #(this will be os.path.join(BASE_DIR, 'templates') in Django<3.1)
            ...
        },
    ]

Create a `templates` directory. Inside, create `base.html`, `users.html` and `profile.html`, `signup.html`, and `login.html`.

    $ mkdir templates
    $ cd templates
    templates $ touch base.html users.html profile.html signup.html login.html

We'll be using Django's template inheritance to keep our HTML simple.

In `base.html`

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <!--load content here-->
        {% block content %}
        {% endblock %}
    </body>
    </html>

In `users.html` and `profile.html`, `

    {% extends 'base.html' %}

    {% block content %}
    {% endblock %}


We'll keep the HTML to a minimum and won't be using any CSS at all, for simplicity.

## Custom User Model

We will need to extend the built-in `AbstractUser` model in order to add extra fields to our user model.

We will be proceeding as if a model was created called `CustomUser` in our `users` app.

A guide for setting up the `CustomUser` model can be found [here](https://github.com/dirtTastesGood/simplified_guides/blob/master/custom_user_model.md).



## PIL

    $ pipenv install pillow

In `profile_images/models.py`:

## Create ProfileImage Model

In `profile_images/models.py`:

    from django.db import models
    import PIL

    class ProfileImage(models.Model):

        image = models.ImageField(
            verbose_name="profile image",
            default="default.jpg",
            upload_to='profile_images/,
        )

        def __str__(self):
            return self.image.name


Let's create out database.

    $ python manage.py makemigrations && python manage.py migrate

And a `superuser`

    $ python manage.py createsuperuser

## Forms

We'll be using various Django form classes to build our forms for uploading and updating profile images as well as creating and signing in users.

### ProfileImage Form

Create `profile_images/forms.py`. Inside we will extend Django's `ModelForm` class to create a form for uploading profile images.

In `profile_images/forms.py`

    from users.models import ProfileImage

    class ProfileImageForm(forms.ModelForm):

        class Meta:
            model = ProfileImage
            fields = ['image']

### User Forms

Create `users/forms.py`. Inside we will extend Django's `UserCreationForm`  class to create users.

In `users/forms.py`:

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


### Template

Break this down into steps:

    <!-- enctype="multipart/form-data" is
    required to be able to upload the file -->
    <form method="POST" enctype="multipart/form-data"> 
        {% csrf_token %}

        <!-- The field label will be styled and used
        as the button to bring up the file select menu.
        An input field with an id of 'id_image' will
        be generated by the Django form rendering -->
        <label for="id_image">
            <p>
                Select profile image
            </p> 

            <!-- This is the original field and will
            be hidden because it looks gross and is
            difficult to customize -->
            <div id="profile-image-field">
                <!-- This will generate the input
                field with an id of 'id_image'-->
                {{ u_form.image }}
            </div>
        </label>

        <!-- Updated with JS to display the name of the file the user selects, if desired. -->
        <div id="new-image">
            No file selected
        </div>

        <!-- Button to submit the form -->
        <button type="submit">
            Update
        </button>
    </form>

- Create `users/urls.py`
- set up urls and views for 
  - signup
  - login
  - profile
  - user-list
- Create sign up/login templates
- Successfully sign up / login users
- Create profile image object on user signup
- upload and rename new photo / replace old user image object on update
- Create UserCreation form and ProfileImageUpdateForm in users/forms.py
- 