from django.db import models

# used for custom user model
from django.contrib.auth.models import AbstractUser

from imagekit.models import ProcessedImageField

from django.urls import reverse

# Create your models here.

# Create a model for posting image and alternative title

class IGUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to='static/images/profiles',
        # image format
        format='JPEG',
        options={'quality':100},
        blank=True,
        null=True
    )

class Post(models.Model):
    author = models.ForeignKey(
        IGUser,
        on_delete=models.CASCADE,
        related_name='my_posts'
    )
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
    
    def get_like_count(self):
        return self.likes.count()
    
    def get_comment_count(self):
        return self.comments.count()



class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes',)
    user = models.ForeignKey(IGUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("post", "user")

    def __str__(self):
        return 'Like: User ' + self.user.username + ' likes [' + self.post.title + '] from User ' + self.post.author.username
    
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',)
    user = models.ForeignKey(
        IGUser,
        on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.comment