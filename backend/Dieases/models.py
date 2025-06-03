from django.db import models

from Doctors.models import Doctor

# Create your models here.

class Dieases(models.Model):
    name = models.CharField(max_length=20)
    DieasesPic = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    treatmentPossible = models.CharField(max_length=255)
    treatmentAvgDuration = models.IntegerField()
    doctors = models.ManyToManyField(Doctor)

    def __str__(self):
        return self.name