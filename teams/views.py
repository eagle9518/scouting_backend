from django.shortcuts import render, get_object_or_404
from teams.models import Teams, Team_Match_Data
from api.tba import get_team_events, get_teams_list, get_match_schedule
from .forms import NewPitScoutingData


def home(request):
    return render(request, 'home.html')


def display_teams(request):
    # Loops through each team for given tournament and creates a Team object from tba.py
    for team in get_teams_list():
        Teams.objects.get_or_create(team_number=team["team_number"])

    all_teams = Teams.objects.order_by("team_number")
    return render(request, 'view_teams.html', {'all_teams': all_teams})


def team_page(request, team_number):
    team, created = Teams.objects.get_or_create(team_number=team_number)
    all_team_match_data = Team_Match_Data.objects.filter(team=team).order_by("quantifier", "-match_number")
    return render(request, 'team_page.html', {'team': team, 'all_team_match_data': all_team_match_data})


def pit_scouting(request):
    if request.method == 'POST':
        form = NewPitScoutingData(request.POST)
    else:
        form = NewPitScoutingData()

    return render(request, "pit_scouting.html", {'form': form})

