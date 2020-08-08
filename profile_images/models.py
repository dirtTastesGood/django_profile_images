from django.db import models

class ProfileImage(models.Model):
    image = models.ImageField(
        verbose_name='profile image',
        default='profile_images/default.jpg',
        upload_to='profile_images'
    )

    def __str__(self):
        return self.image.name

