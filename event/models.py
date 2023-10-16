from django.db import models
from user.models import User
from django.core.exceptions import ValidationError


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

    def clean(self):
        # Ensure end_datetime is greater than start_datetime
        if self.end_datetime <= self.start_datetime:
            raise ValidationError("End datetime must be greater than start datetime")

    def save(self, *args, **kwargs):
        self.clean()  # Call the clean method before saving
        super(Event, self).save(*args, **kwargs)
