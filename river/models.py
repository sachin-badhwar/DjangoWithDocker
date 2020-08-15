from django.db import models

# Create your models here.
class FamilyRooms(models.Model):
    pic = models.ImageField()
    description = models.CharField(max_length=100)

class DeluxRooms(models.Model):
    pic = models.ImageField()
    description = models.CharField(max_length=100)

class SpecialRooms(models.Model):
    pic = models.ImageField()
    description = models.CharField(max_length=100)    