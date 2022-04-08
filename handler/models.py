from django.db import models

class Stock(models.Model):
    datetime = models.DateTimeField()
    close = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    open = models.FloatField()
    volume = models.IntegerField()
    instrument = models.CharField(max_length=100)