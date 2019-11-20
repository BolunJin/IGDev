from django.db import models

# used for custom user model
from django.contrib.auth.models import AbstractUser

from imagekit.models import ProcessedImageField

from django.urls import reverse

# Create your models here.

# Create a model for posting image and alternative title
class Post(models.Model):
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        # storage address when usr upload an image
        upload_to='static/images/posts',
        # image format
        format='JPEG',
        options={'quality':100},
        blank=True,
        null=True
    )

    # After user submit a create form, need an url to redirect
    def get_absolute_url(self):
        # traceback url correspond to name "[string]"
        # provide params in list to url
        return reverse("post_detail", args=[str(self.id)]) 

class IGUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to='static/images/profiles',
        # image format
        format='JPEG',
        options={'quality':100},
        blank=True,
        null=True
    )