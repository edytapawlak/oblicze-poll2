from django.db import models
from activities.models import Lecture, Poster

# Create your models here.
class ChoosedLecture(models.Model):
    lecture = models.ForeignKey(Lecture)
    
    def __str__(self):
        return str(self.lecture)

class ChoosedPoster(models.Model):
    poster = models.ForeignKey(Poster)

    def __str__(self):
        return str(self.poster)
