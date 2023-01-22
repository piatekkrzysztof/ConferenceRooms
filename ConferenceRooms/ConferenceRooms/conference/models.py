from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField()
    projector = models.BooleanField()

class Reservation(models.Model):
    data = models.DateTimeField()
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    comment = models.CharField(max_length=128, null=True)

    class Meta:
        unique_together=('room_id', 'data')



