from django.shortcuts import render

from api.tba import get_match_schedule, get_single_match
from teams import models
from django.db.models import Avg


def rankings(request):
    teams = models.Teams.objects.all().order_by("team_number")
    team_averages = {}
    for team in teams:
        team_averages[team.team_number] = fetch_team_match_averages(team.team_number)

    return render(request, "strategy/rankings.html", {'team_averages': team_averages})


def dashboard(request):
    match = get_single_match("qm1")
    red_json = {}
    blue_json = {}
    for red_team in match['red']:
        red_json[red_team] = fetch_team_match_averages(red_team)
    for blue_team in match['blue']:
        blue_json[blue_team] = fetch_team_match_averages(blue_team)

    return render(request, "strategy/dashboard.html", {'red_alliance': red_json, 'blue_alliance': blue_json})


def picklist(request):
    return render(request, "strategy/picklist.html")


def fetch_team_match_averages(team):
    team_match_data = models.Team_Match_Data.objects.filter(team=models.Teams.objects.get(team_number=team))
    team_match_averages = team_match_data.aggregate(Avg('auto_amp', default=0),
                                                    Avg('auto_speaker_make', default=0),
                                                    Avg('teleop_amp', default=0),
                                                    Avg('teleop_speaker_make', default=0),
                                                    Avg('trap', default=0),
                                                    Avg('climb', default=0))

    return {'auto': team_match_averages['auto_amp__avg'] + team_match_averages['auto_speaker_make__avg'],
            'teleop': team_match_averages['teleop_amp__avg'] + team_match_averages['teleop_speaker_make__avg'],
            'trap': team_match_averages['trap__avg'],
            'climb': team_match_averages['climb__avg']}
