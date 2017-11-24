from django.db import models

# Create your models here.

class Date(models.Model):
    date = models.DateField()

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")

class Place(models.Model):
    place = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.place

class Schedule(models.Model):
    start = models.TimeField()
    end = models.TimeField()
    date = models.ForeignKey(Date)
    place = models.ForeignKey(Place)
    
    def __str__(self):
        return '  '.join([str(self.date), str(self.place), self.start.strftime("%H:%M")])
