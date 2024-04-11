from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    #Add more fields as needed

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(Movie, on_delete=models.CASCADE)
    