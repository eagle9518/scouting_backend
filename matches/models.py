from django.db import models


# Create your models here.
class Matches(models.Model):
    quantifier = models.CharField(max_length=10)
    match_number = models.IntegerField()
    red_one = models.IntegerField()
    red_two = models.IntegerField()
    red_three = models.IntegerField()
    blue_one = models.IntegerField()
    blue_two = models.IntegerField()
    blue_three = models.IntegerField()
