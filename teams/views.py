from django.shortcuts import render, get_object_or_404, redirect

from scouting_backend import settings
from teams.models import Teams, Team_Match_Data
from api.tba import get_team_events, get_teams_list, get_match_schedule
from .forms import NewPitScoutingData


def home(request):
    return render(request, 'home.html')


def display_teams(request):
    # Loops through each team for given tournament and creates a Team object from tba.py
    for team in get_teams_list():
        if not Teams.objects.filter(team_number=team["team_number"]).exists():
            Teams.objects.create(team_number=team["team_number"], pit_scout_status=False)

    all_teams = Teams.objects.order_by("team_number")
    return render(request, 'teams/view_teams.html', {'all_teams': all_teams})


def team_page(request, team_number):
    team, created = Teams.objects.get_or_create(team_number=team_number)
    all_team_match_data = Team_Match_Data.objects.filter(team=team).order_by("quantifier", "-match_number")
    return render(request, 'teams/team_page.html', {'team': team, 'all_team_match_data': all_team_match_data})


def pit_scouting(request, team_number):
    if request.method == 'POST':
        form = NewPitScoutingData(request.POST, request.FILES)
        if form.is_valid():
            Teams.objects.filter(team_number=team_number).update(
                drivetrain=form.cleaned_data.get('drivetrain'),
                weight=form.cleaned_data.get('weight'),
                length=form.cleaned_data.get('length'),
                width=form.cleaned_data.get('width'),
                robot_picture=form.cleaned_data.get('robot_picture'),
                additional_info=form.cleaned_data.get('additional_info'),
                pit_scout_status=True
            )
            return redirect("teams")
    else:
        form = NewPitScoutingData()
    return render(request, "teams/pit_scouting.html", {'form': form, 'team_number': team_number})

