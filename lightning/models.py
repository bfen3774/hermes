from django.db import models

# Create your models here.

class Plan(models.Model):
    name = models.CharField(max_length=300)
    reddit_link = models.URLField(max_length=200)
    user = models.CharField(max_length=200)
    user_age = models.CharField(max_length=100)
    user_sex = models.CharField(max_length=20)
    user_height = models.IntegerField()
    user_body_type_start = models.CharField(max_length=200)
    user_body_type_end = models.CharField(max_length=200)
    user_starting_weight = models.IntegerField()
    user_ending_weight = models.IntegerField()
    goals = models.CharField(max_length=100)

class Diet(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    calories = models.IntegerField()
    name = models.CharField(max_length=100)
    macro_protein = models.IntegerField()
    macro_carb = models.IntegerField()
    macro_fat = models.IntegerField()
