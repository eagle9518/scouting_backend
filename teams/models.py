from django.db import models
from django.db.models import Model


class Teams(models.Model):
    team_number = models.IntegerField(unique=True)
    # robot_picture = models.ImageField()
    # drivetrain = models.CharField(max_length=32)
    # primary_role = models.CharField(max_length=32)
    # additional_info = models.CharField(max_length=128)


class Team_Match_Data(models.Model):
    match = models.ForeignKey(Teams, related_name='match_data', on_delete=models.CASCADE)
    match_number = models.IntegerField()
    auto_charging_station = models.IntegerField()
    auto_cones = models.IntegerField()
    auto_cubes = models.IntegerField()
    teleop_cones = models.IntegerField()
    teleop_cubes = models.IntegerField()
    cone_transport = models.IntegerField()
    cube_transport = models.IntegerField()
    end_charging_station = models.IntegerField()
    total_points = models.IntegerField()
    driver_ranking = models.IntegerField()
    defense_ranking = models.IntegerField()
    comment = models.CharField(max_length=128)
    scout_name = models.CharField(max_length=32)


