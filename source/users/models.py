"""
Models for the users app
"""

from PIL import Image
import os

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Profile model for user"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default="profile_pics/default.jpg", upload_to="profile_pics"
    )

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self):
        if self.pk:
            try:
                old_image = Profile.objects.get(pk=self.pk)
                if (
                    old_image.image != self.image
                    and old_image.image.name != "default.jpg"
                ):
                    if os.path.isfile(old_image.image.path):
                        os.remove(old_image.image.path)
            except Profile.DoesNotExist:
                pass

        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
