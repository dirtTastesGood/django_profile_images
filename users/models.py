from django.db import models
from django.contrib.auth.models import AbstractUser
from profile_images.models import ProfileImage

class CustomUser(AbstractUser):
    profile_image = models.OneToOneField(
        ProfileImage,
        null=True,
        on_delete = models.SET_NULL
    )

    def has_profile_image(self):
        return self.profile_image is not None

    def __str__(self):
        return self.username