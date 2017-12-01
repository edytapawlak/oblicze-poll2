from django.db import models
from activities.models import Lecture

# Create your models here.
class ChoosedLecture(models.Model):
    lecture = models.ForeignKey(Lecture)
    
    def __str__(self):
        return str(self.lecture)
