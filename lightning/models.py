from django.db import models

# Create your models here.

class Plan(models.Model):
    name = models.CharField(max_length=300)
    reddit_link = models.URLField(max_length=200)
    user = models.CharField(max_length=200)
    user_age = models.CharField(max_length=100)
    user_starting_weight = models.IntegerField()
    user_ending_weight = models.IntegerField()

