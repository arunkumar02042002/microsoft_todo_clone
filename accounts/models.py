from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    bio = models.CharField(max_length=255, blank=True)
    profile_img = models.ImageField(upload_to='users/profile_images', default='blank-profile-picture.png')

    def save(self, *args, **kwargs):
        # If bio is not provided, set a default bio based on the first_name
        if not self.bio and self.first_name:
            self.bio = f"I'm {self.first_name}."
        super().save(*args, **kwargs)