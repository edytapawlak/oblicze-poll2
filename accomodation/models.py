from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dinner(models.Model):
    remark = models.CharField(max_length = 100)
    date = models.DateField()
    vege = models.BooleanField()
    user = models.ForeignKey(User)
