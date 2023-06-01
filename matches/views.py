import numpy as np
from django.http import JsonResponse
from django.shortcuts import render

from api.tba import get_match_schedule
from matches.models import Matches
from teams.models import Teams, Team_Match_Data

comp_level_dic = {"qm": "Quals", "sf": "Playoff", "f": "Finals"}


def matches_list(request):
    # Loops through each match for given tournament - in tba.py
    for match in get_match_schedule():
        # Grabs match quantifier from tba data and maps it correctly via dictionary
        quantifier = comp_level_dic[match["comp_level"]]
        if quantifier == "Playoff":
            match_number = match["set_number"]
        else:
            match_number = match["match_number"]

        # Creates a new Match object with given data if it doesn't exist
        Matches.objects.get_or_create(quantifier=quantifier,
                                      match_number=match_number,
                                      red_one=int(match["alliances"]["red"]["team_keys"][0].replace("frc", "")),
                                      red_two=int(match["alliances"]["red"]["team_keys"][1].replace("frc", "")),
                                      red_three=int(match["alliances"]["red"]["team_keys"][2].replace("frc", "")),
                                      blue_one=int(match["alliances"]["blue"]["team_keys"][0].replace("frc", "")),
                                      blue_two=int(match["alliances"]["blue"]["team_keys"][1].replace("frc", "")),
                                      blue_three=int(match["alliances"]["blue"]["team_keys"][2].replace("frc", "")))
    all_matches = Matches.objects.order_by("quantifier", "match_number")
    return render(request, 'matches_list.html', {'matches': all_matches})


def match_summaries(request, quantifier, match_number, team_number):
    match = Matches.objects.get(quantifier=quantifier, match_number=match_number)
    all_teams_in_match = [match.red_one, match.red_two, match.red_three, match.blue_one, match.blue_two, match.blue_three]

    # team_data = Team_Match_Data.objects.get(team=Teams.objects.get_or_create(team_number=match_data_wanted), match_number=match_number)
    team, created = Teams.objects.get_or_create(team_number=359)
    team_match_data = Team_Match_Data.objects.get(team=team, match_number=2)
    scoring_grid = [team_match_data.auto_upper, team_match_data.auto_middle, team_match_data.auto_lower,
                    team_match_data.teleop_upper, team_match_data.teleop_middle, team_match_data.teleop_lower]
    return render(request, 'match_summaries.html', {"match": match, "all_teams_in_match": all_teams_in_match, "team_number": team_number, "scoring_grid": scoring_grid})
