from django.shortcuts import render
from teams import models
from django.db.models import Avg


def rankings(request):
    # teams = models.Teams.objects.all()
    # d = {}
    # for team in teams:
    #     d[team.team_number] = []
    #     team_matches = models.Team_Match_Data.objects.filter(team=team)
    #     d[team.team_number].append(team_matches.aggregate(Avg('auto_amp'))['auto_amp'] + team_matches.aggregate(Avg('auto_speaker_make'))['auto_speaker_make'])
    #     d[team.team_number].append(team_matches.aggregate(Avg('teleop_amp'))['teleop_amp'] + team_matches.aggregate(Avg('teleop_speaker_make'))['teleop_speaker_make'])
    #     d[team.team_number].append(team_matches.aggregate(Avg('trap'))['trap'])
    #     d[team.team_number].append(team_matches.aggregate(Avg('climb'))['climb'])
    d = models.Team_Match_Data.objects.filter(team=models.Teams.objects.get(team_number=498)).aggregate(average_notes=Avg('auto_amp'))['average_notes']

    return render(request, "rankings.html", {'d': d})


def dashboard(request):
    return render(request, "dashboard.html")


def picklist(request):
    return render(request, "picklist.html")


