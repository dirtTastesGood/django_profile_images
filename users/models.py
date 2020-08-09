from django.db import models
from django.contrib.auth.models import AbstractUser
from profile_images.models import ProfileImage

class CustomUser(AbstractUser):
    profile_image = models.OneToOneField(
        ProfileImage,
        default=1,
        on_delete = models.SET_DEFAULT,
    )

    def set_profile_image(self, new_image):
        pass


    def __str__(self):
        return self.username