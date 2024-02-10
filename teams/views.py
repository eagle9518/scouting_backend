import os

import cloudinary
import cloudinary.api
import cloudinary.uploader
from django.shortcuts import render, redirect

from api.tba import get_teams_list
from teams.models import Teams, Team_Match_Data
from .forms import NewPitScoutingData

cloudinary.config(
    cloud_name=os.environ.get("CLOUD_NAME"),
    api_key=os.environ.get("CLOUD_API_KEY"),
    api_secret=os.environ.get("CLOUD_API_SECRET"),
    secure=True
)


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
            image_response = cloudinary.uploader.upload(request.FILES['robot_picture'])
            img_url = image_response["secure_url"]
            image_url_list = img_url.split("upload/")
            image_url_list.insert(1, "upload/w_0.4,c_scale/")
            img_url = "".join(image_url_list)

            Teams.objects.filter(team_number=team_number).update(
                drivetrain=form.cleaned_data.get('drivetrain'),
                weight=form.cleaned_data.get('weight'),
                length=form.cleaned_data.get('length'),
                width=form.cleaned_data.get('width'),
                robot_picture=img_url,
                additional_info=form.cleaned_data.get('additional_info'),
                pit_scout_status=True
            )
            return redirect("team_page", team_number=team_number)
    else:
        form = NewPitScoutingData()
    return render(request, "teams/pit_scouting.html", {'form': form, 'team_number': team_number})
