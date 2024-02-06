from django.shortcuts import render
from teams import models
from django.db.models import Avg


def rankings(request):
    teams = models.Teams.objects.all()
    team_averages = {}
    for team in teams:
        team_match_data = models.Team_Match_Data.objects.filter(team=team)
        if team_match_data.exists():
            team_match_averages = team_match_data.aggregate(Avg('auto_amp'), Avg('auto_speaker_make'), Avg('teleop_amp'), Avg('teleop_speaker_make'), Avg('trap'), Avg('climb'))
            team_averages[team.team_number] = [team.team_number,
                                               team_match_averages['auto_amp__avg'] + team_match_averages['auto_speaker_make__avg'],
                                               team_match_averages['teleop_amp__avg'] + team_match_averages['teleop_speaker_make__avg'],
                                               team_match_averages['trap__avg'],
                                               team_match_averages['climb__avg']]

    return render(request, "rankings.html", {'team_averages': team_averages})


def dashboard(request):
    return render(request, "dashboard.html")


def picklist(request):
    return render(request, "picklist.html")


