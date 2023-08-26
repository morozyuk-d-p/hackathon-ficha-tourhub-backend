from django.db import models
from maps.models import Location

# Create your models here.
class Event(models.Model):
    place = models.ForeignKey(Location, verbose_name='Место', on_delete=models.CASCADE)
    startTime = models.DateTimeField(verbose_name='Время начала')
    endTime = models.DateTimeField(verbose_name='Время конца')

    class Meta:
        verbose_name = 'событие'
        verbose_name_plural = 'события'
        