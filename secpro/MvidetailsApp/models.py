from django.db import models

# Create your models here.
class Moviedetails(models.Model):
    moviename = models.CharField(max_length=100)
    budjet = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    hero = models.CharField(max_length=100)
    heroine = models.CharField(max_length=100)