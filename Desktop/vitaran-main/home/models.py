from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

###isko badal   
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

CHOICES =( 
    ("1", "yes"), 
    ("0", "No"), 
) 


class Orders(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    order_to =models.CharField(default='new delhi',max_length=1000)
    order_from =models.CharField(default='aya nagar',max_length=1000)
    approx_weight = models.IntegerField(default=10)
    approx_size =models.CharField(default='input size here',max_length=1000)
    description =models.TextField(default='input details here',max_length=1000)
    order_image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bidding_choice= models.CharField(choices =CHOICES,default = '1',max_length=5) 

    def __str__(self):
        return f'{self.user.username} order'

    def save(self, *args, **kwargs):
        super().save()



