from django.db import models
from django.db.models import Model


class Teams(models.Model):
    team_number = models.IntegerField(unique=True)
    robot_picture = models.ImageField(blank=True, null=True)
    drivetrain = models.CharField(max_length=32)
    weight = models.IntegerField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    additional_info = models.CharField(max_length=256, blank=True, null=True)
    pit_scout_status = models.BooleanField()


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
    comment = models.CharField(max_length=256)
    scout_name = models.CharField(max_length=32)
