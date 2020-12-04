from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone_number = models.IntegerField(default=132)
    adhar_card_number = models.IntegerField(default=551)
    adhar_image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    pan_card_number = models.CharField(default=551,max_length=10)
    pan_image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    preferd_vehical_type = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



