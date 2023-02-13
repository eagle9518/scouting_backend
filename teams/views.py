from django.shortcuts import render

# Create your views here.
from teams.models import Teams


def display_teams(request):
    if not Teams.objects.filter(team_number=2073).exists():
        Teams.objects.create(team_number=2073)
    all_teams = Teams.objects.all()
    return render(request, 'view_teams.html', {'all_teams': all_teams})


def team_page(request, team_number):
    team = Teams.objects.get(team_number=team_number)
    return render(request, 'team_page.html', {'team': team})
