from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    institute = models.CharField(max_length = 100, default = '')

def create_profile(sender, **kwargs):
    if(kwargs['created']):
            profile = UserProfile.objects.create(user = kwargs['instance'])


post_save.connect(create_profile, sender = User)

