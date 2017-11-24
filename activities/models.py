from django.db import models
from django.contrib.auth.models import User
from schedule.models import Schedule

class Tag(models.Model):
    title = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.title

class Lecture(models.Model):
    title = models.CharField(max_length = 500)
    abstract = models.CharField(max_length = 1000)
    tags = models.ManyToManyField(Tag)
    schedule = models.ForeignKey(Schedule, null = True, blank = True)
    
    def __str__(self):
        return ' -- '.join([str( Author.objects.get(lecture_id = self)), self.title])


class Poster(models.Model):
    title = models.CharField(max_length = 500)
    abstract = models.CharField(max_length = 1000)
    tags = models.ManyToManyField(Tag)
    schedule = models.ForeignKey(Schedule, null = True, blank = True)  

class Author(models.Model):
    user = models.ForeignKey(User)
    poster_id = models.ForeignKey(Poster, null = True)
    lecture_id = models.ForeignKey(Lecture, null = True)

    def __str__(self):
        return ' '.join([self.user.first_name, self.user.last_name])

class Break(models.Model):
    title = models.CharField(max_length = 300)
    schedule = models.ForeignKey(Schedule)
