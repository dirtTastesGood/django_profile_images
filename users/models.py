from django.db import models
from django.contrib.auth.models import AbstractUser
from profile_images.models import ProfileImage

class CustomUser(AbstractUser):
    profile_image = models.ForeignKey(
        ProfileImage,
        default=1,
        on_delete = models.SET_DEFAULT,
    )

    def __str__(self):
        return self.username