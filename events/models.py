from django.db import models

# Create your models here.


class Event(models.Model):

    title=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    date=models.DateField()
    time=models.TimeField()
    venue=models.CharField(max_length=100)
    registration_deadline=models.DateField()
    max_participants=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
