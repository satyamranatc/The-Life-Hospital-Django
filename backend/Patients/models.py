from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=20)
    ProfilePic = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    admitDate = models.DateField()
    diease = models.ManyToManyField('Dieases.Dieases')
    # doctor = models.ManyToManyField('Doctors.Doctor')
