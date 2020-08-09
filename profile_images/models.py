from django.db import models

class ProfileImage(models.Model):
    image = models.ImageField(
        verbose_name='profile image',
        default='default.jpg',
        upload_to='profile_images'
    )

    def __str__(self):
        return f'{self.image.name}'

