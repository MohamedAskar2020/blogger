from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    post_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        
        ordering = ('-post_date',)
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title

#===============================================================

class Comment(models.Model):

    name = models.CharField(max_length=50, verbose_name="الاسم")
    email = models.EmailField(verbose_name='البريد الالكتروني')
    body = models.TextField(verbose_name='التعليق')
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        
        ordering = ('-comment_date',)
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")

    def __str__(self):
        return 'علق {} على {}.' .format(self.name, self.post)


