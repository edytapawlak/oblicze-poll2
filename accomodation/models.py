from django.db import models
from django.contrib.auth.models import User


class Dinner(models.Model):
    date = models.DateField(default = '10/10/10')
    vege = models.BooleanField(default = False)
    remark = models.CharField(max_length = 500)
    user = models.ForeignKey(User)

class Hostel(models.Model):
    date = models.DateField()
    hostel_name = models.CharField(max_length = 100, blank = True)
    user = models.ForeignKey(User)

