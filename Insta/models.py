from django.db import models
from imagekit.models import ProcessedImageField
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.
class InstaUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to='static/images/profiles',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True,
     )

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
    author = models.ForeignKey(
        InstaUser,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='insta_posts',
     )
    posted_on=models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=True,
        null=True
     )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.pk})
    def get_like_count(self):
        return self.likes.count()
    def get_comment_count(self):
        return self.comments.count



class Comment(models.Model):
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, 
        related_name='comments',)
    user = models.ForeignKey(
        InstaUser, 
        on_delete=models.CASCADE, 
        related_name='comments',)
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(
        auto_now_add=True, 
        editable=False)

    def __str__(self):
        return self.comment

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes',)
    user = models.ForeignKey(InstaUser, on_delete=models.CASCADE)

    def __str__(self):
        return 'Like: ' + self.user.username + ' likes ' + self.post.title