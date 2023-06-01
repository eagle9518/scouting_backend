from django.shortcuts import render, get_object_or_404

# Create your views here.
from teams.models import Teams
from api.tba import get_team_events, get_teams_list, get_match_schedule


def home(request):
    return render(request, 'index.html')


def display_teams(request):
    for team in get_teams_list():
        Teams.objects.get_or_create(team_number=team["team_number"])

    all_teams = Teams.objects.all().order_by("team_number")
    return render(request, 'view_teams.html', {'all_teams': all_teams})


def team_page(request, team_number):
    team, created = Teams.objects.get_or_create(team_number=team_number)

    return render(request, 'team_page.html', {'team': team})
