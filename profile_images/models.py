from django.db import models
from pathlib import Path

def get_upload_path(instance, filename):
    ''' Calculate and return an upload path for a profile image
        which includes the user's username '''
    # get the file's extension 
    file_extension = filename.split('.')[-1]

    # upload to profile_images/<USERNAME>/
    file_path = Path(f'profile_images/{instance.customuser.username}/profile_image.{file_extension}') 
    
    # file path must be a string
    return str(file_path)

class ProfileImage(models.Model):
    image = models.ImageField(
        verbose_name='profile image',
        default='default.jpg',
        upload_to=get_upload_path,
    )

    def __str__(self):
        return f'{self.image.name}'

