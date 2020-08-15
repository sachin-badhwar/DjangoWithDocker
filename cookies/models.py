from django.db import models
from django.utils import timezone
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=30)

class Languages(models.Model):
    name = models.CharField(max_length=50)
    creator = models.CharField(null=True,max_length=50)
    paradigm = models.CharField(null=True,max_length=50)
    published_date = models.DateTimeField(blank=True, null=True)
    published = models.DateField(blank=True, null=True)

    @classmethod
    def publish(self):
        #published_date = timezone.now()
        return '2020-08-15'
        
        #self.save()
        #return published_date

    def __str__(self):
        return self.name

class Programmers(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    company_name = models.ForeignKey(Company,on_delete=models.CASCADE)
    language = models.ManyToManyField(Languages)

    def __str__(self):
        return self.name

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.name        

class JobApplicants(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    image = models.ImageField(null=True, blank=True)
    resume = models.FileField(null=True, blank=True)        