from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=256)
    measurements = models.ManyToManyField(Measurement, blank=True)
