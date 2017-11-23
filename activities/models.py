from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    title = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.title

class Lecture(models.Model):
    title = models.CharField(max_length = 500)
    abstract = models.CharField(max_length = 1000)
    tags = models.ManyToManyField(Tag)
#    shedule = 

class Poster(models.Model):
    title = models.CharField(max_length = 500)
    abstract = models.CharField(max_length = 1000)
    tags = models.ManyToManyField(Tag)
#   shedule = 

class Author(models.Model):
    user = models.ForeignKey(User)
    poster_id = models.ForeignKey(Poster, null = True)
    lecture_id = models.ForeignKey(Lecture, null = True)

