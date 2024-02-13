import json

from django.db.models import Avg
from django.http import JsonResponse
from django.shortcuts import render

from api.tba import get_single_match
from teams import models

from helpers import login_required


def rankings(request):
    comp_code = request.GET.get('comp')
    teams = models.Teams.objects.filter(event=comp_code).order_by("team_number")
    team_averages = {}
    for team in teams:
        team_averages[team.team_number] = fetch_team_match_averages(team.team_number)

    return render(request, "strategy/rankings.html", {'team_averages': team_averages})


def dashboard(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        match_number = json.load(request)
        match = get_single_match(request.GET.get('comp'), "qm" + str(match_number))
        red_json = {}
        red_teams = []
        blue_json = {}
        blue_teams = []
        for red_team in match['red']:
            red_json[red_team] = fetch_team_match_averages(red_team)
            red_teams.append(red_team)
        for blue_team in match['blue']:
            blue_json[blue_team] = fetch_team_match_averages(blue_team)
            blue_teams.append(blue_team)

        response = {'red': red_json, 'blue': blue_json, 'red_teams': red_teams, 'blue_teams': blue_teams}
        return JsonResponse(response)

    return render(request, "strategy/dashboard.html")


def picklist(request):
    return render(request, "strategy/picklist.html")


def fetch_team_match_averages(team_number):
    team_match_data = models.Team_Match_Data.objects.filter(team_number=team_number)
    team_match_averages = team_match_data.aggregate(Avg('auto_amp', default=0),
                                                    Avg('auto_speaker_make', default=0),
                                                    Avg('teleop_amp', default=0),
                                                    Avg('teleop_speaker_make', default=0),
                                                    Avg('trap', default=0),
                                                    Avg('climb', default=0))

    return {'team_number': team_number,
            'auto': team_match_averages['auto_amp__avg'] + team_match_averages['auto_speaker_make__avg'],
            'teleop': team_match_averages['teleop_amp__avg'] + team_match_averages['teleop_speaker_make__avg'],
            'trap': team_match_averages['trap__avg'],
            'climb': team_match_averages['climb__avg']}
