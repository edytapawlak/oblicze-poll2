from django.db import models
from django.contrib.auth.models import User
from activities.models import Lecture, Poster

# Create your models here.
class Status(models.Model):
    poll_status = models.BooleanField(default = False)

class LectureRating(models.Model):
    user = models.ForeignKey(User)
    lecture = models.ForeignKey(Lecture)
    rate = models.IntegerField()

class PosterRating(models.Model):
    user = models.ForeignKey(User)
    poster= models.ForeignKey(Poster)
    rate = models.IntegerField()
