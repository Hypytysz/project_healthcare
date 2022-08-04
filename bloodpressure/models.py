from django.db import models

# Create your models here.
class Bloodpressure(models.Model):
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    pulse = models.IntegerField()
    data = models.DateTimeField()
    description = models.TextField()