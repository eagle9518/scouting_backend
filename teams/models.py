from django.core.validators import validate_comma_separated_integer_list
from django.db import models
from django.db.models import Model
from matches.models import Matches 


class Teams(models.Model):
    team_number = models.IntegerField(unique=True)
    robot_picture = models.ImageField()
    drivetrain = models.CharField(max_length=32)
    primary_role = models.CharField(max_length=32)
    additional_info = models.CharField(max_length=128)


# TODO Somehow connect quantifier and match_number to Matches via Foreign Key...
class Team_Match_Data(models.Model):
    team = models.ForeignKey(Teams, related_name='team_match_data', on_delete=models.CASCADE)
    match_number = models.IntegerField()
    quantifier = models.CharField(max_length=10)

    auto_leave = models.IntegerField()
    auto_amp = models.IntegerField()
    auto_speaker_make = models.IntegerField()
    auto_speaker_miss = models.IntegerField()

    teleop_amp = models.IntegerField()
    teleop_speaker_make = models.IntegerField()
    teleop_speaker_miss = models.IntegerField()

    trap = models.IntegerField()
    climb = models.IntegerField()

    driver_ranking = models.IntegerField()
    defense_ranking = models.IntegerField()
    comment = models.CharField(max_length=128)
    scout_name = models.CharField(max_length=32)
