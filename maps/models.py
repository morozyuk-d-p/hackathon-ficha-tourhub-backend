from django.db import models

# Create your models here.
class Location(models.Model):
    def __str__(self) -> str:
        return self.name
    
    name = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание', max_length=500, default=None, blank=True)
    latitude = models.DecimalField(verbose_name='Широта', decimal_places=6, max_digits=9)
    longitude = models.DecimalField(verbose_name='Долгота', decimal_places=6, max_digits=9)

    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'места'
        