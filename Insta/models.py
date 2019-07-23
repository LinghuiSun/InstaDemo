from django.db import models
from imagekit.models import ProcessedImageField
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Post(models.Model):
    title = models.TextField(blank=True, null = True)
    image = ProcessedImageField(
        upload_to='static/images/posts',
        # processors=[ResizeToFill(100, 50)],
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True,
     )
    def __str__(self):
         return self.title
    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.pk})

class InstaUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to='static/images/profiles',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True,
     )