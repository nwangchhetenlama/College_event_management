from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Event(models.Model):

    title=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    date=models.DateField()
    time=models.TimeField()
    venue=models.CharField(max_length=100)
    registration_deadline=models.DateField()
    max_participants=models.IntegerField()
    banner=models.ImageField(upload_to="event_banners/",null=True,blank=True)


    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
class EventRegistration(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    event=models.ForeignKey(Event, on_delete=models.CASCADE)
    registered_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=('user','event')

    def __str__(self):
        return f"{self.user.username}->{self.event.title}"
    

