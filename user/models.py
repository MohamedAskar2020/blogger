from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image

# Create your models here.

class Profile(models.Model):

    image = models.ImageField(
        default='profile_pics/man-person-icon.png', upload_to='profile_pics')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.width > 300 or img.height > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def create_profile(sender, **kwargs):
        
        if kwargs['created']:
            user_profile = Profile.objects.create(user=kwargs['instance'])
    post_save.connect(create_profile, User)
        
