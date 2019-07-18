from django.db import models
from imagekit.models import ProcessedImageField
# Create your models here.
class Post(models.Model):
    title = models.TextField(blank=True, null = True)
    image = ProcessedImageField(
        upload_to='statics/images/posts',
        # processors=[ResizeToFill(100, 50)],
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True,
     )
    def __str__(self):
         return self.title