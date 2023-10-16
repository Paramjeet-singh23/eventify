from django.db import models
from user.models import User


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    fee = models.IntegerField()

    class Meta:
        db_table = 'event'
