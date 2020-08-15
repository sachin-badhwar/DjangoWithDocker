from django.db import models

# Create your models here.
class Movie(models.Model):
    type_choices = (
        ('Drama','Drama'),
         ('Suspense','Suspence'),
         ('Thriller','Thriller'),
         ('Love','Love'),
         ('Si-Fi','Si-Fi'),
         ('Action','Action'),
         ('Comedy','Comedy')
    )
    name = models.CharField(max_length=30)
    types = models.CharField(max_length=30,choices=type_choices,default='Action')

class Character(models.Model):
    name = models.CharField(max_length=30)
    character_type = models.ForeignKey(Movie,on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie,related_name='Character')
    