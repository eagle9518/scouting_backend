from django.db import models
from django.db.models import Model


class Teams(models.Model):
    team_number = models.IntegerField()
    event = models.CharField(max_length=16, default="testing")
    robot_picture = models.URLField(blank=True, null=True)
    drivetrain = models.CharField(max_length=32)
    weight = models.IntegerField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    additional_info = models.CharField(max_length=256, blank=True, null=True)
    pit_scout_status = models.BooleanField(default=False)


class Team_Match_Data(models.Model):
    team_number = models.IntegerField()
    event = models.CharField(max_length=16, default="testing")
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

    human_player_timing = models.IntegerField(default=-1)
    human_player_spotlit = models.IntegerField(default=-1)
    strategist_name = models.CharField(max_length=32, default="")
