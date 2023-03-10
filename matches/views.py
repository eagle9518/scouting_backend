import json

import numpy as np
from django.http import JsonResponse
from django.shortcuts import render

from api.tba import get_match_schedule
from json import dumps

# Create your views here.
from matches.models import Matches
from teams.models import Teams, Team_Match_Data

comp_level_dic = {"qm": "Quals", "qf": "Quarters", "sf": "Semis", "f": "Finals"}


def matches_list(request):
    for match in get_match_schedule():

        if comp_level_dic[match["comp_level"]] == "Quals" or comp_level_dic[match["comp_level"]] == "Finals":
            quantifier = comp_level_dic[match["comp_level"]]
        else:
            quantifier = "{comp_level}_{set_number}".format(comp_level=comp_level_dic[match["comp_level"]],
                                                            set_number=str(match["set_number"]))

        if not Matches.objects.filter(quantifier=quantifier, match_number=match["match_number"]).exists():
            Matches.objects.create(quantifier=quantifier,
                                   match_number=match["match_number"],
                                   red_one=int(match["alliances"]["red"]["team_keys"][0].replace("frc", "")),
                                   red_two=int(match["alliances"]["red"]["team_keys"][1].replace("frc", "")),
                                   red_three=int(match["alliances"]["red"]["team_keys"][2].replace("frc", "")),
                                   blue_one=int(match["alliances"]["blue"]["team_keys"][0].replace("frc", "")),
                                   blue_two=int(match["alliances"]["blue"]["team_keys"][1].replace("frc", "")),
                                   blue_three=int(match["alliances"]["blue"]["team_keys"][2].replace("frc", "")))
    all_matches = Matches.objects.order_by("quantifier", "match_number")
    return render(request, 'matches_list.html', {'matches': all_matches})


def match_summaries(request, quantifier, match_number, match_data_wanted):
    match = Matches.objects.get(quantifier=quantifier, match_number=match_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if Team_Match_Data.objects.filter(match_number=match_number).exists():
            if match_data_wanted == "Red_Total":
                red_one_match_data = Team_Match_Data.objects.get(team=Teams.objects.get(team_number=match.red_one), match_number=match_number)
                red_two_match_data = Team_Match_Data.objects.get(team=Teams.objects.get(team_number=match.red_two), match_number=match_number)
                red_three_match_data = Team_Match_Data.objects.get(team=Teams.objects.get(team_number=match.red_three), match_number=match_number)
                team_match_data = np.add([red_one_match_data.auto_upper, red_one_match_data.auto_middle, red_one_match_data.auto_lower], np.add(red_two_match_data, red_three_match_data))
            elif match_data_wanted == "Blue_Total":
                blue_one_match_data = Team_Match_Data.objects.get(team=Teams.objects.get(team_number=match.blue_one), match_number=match_number)
                blue_two_match_data = Team_Match_Data.objects.get(team=Teams.objects.get(team_number=match.blue_two), match_number=match_number)
                blue_three_match_data = Team_Match_Data.objects.get(team=Teams.objects.get(team_number=match.blue_three), match_number=match_number)
                team_match_data = np.add(blue_one_match_data, blue_two_match_data, blue_three_match_data).tolist()
            else:
                team_match_data = Team_Match_Data.objects.get(team=Teams.objects.get(team_number=match_data_wanted), match_number=match_number)
            response = {"match_data": [team_match_data.auto_upper, team_match_data.auto_middle, team_match_data.auto_lower]}
        else:
            response = {"match_data": [[0] * 9, [0] * 9, [0] * 9]}

        return JsonResponse(response)

    return render(request, 'match_summaries.html', {"match": match, "match_data_wanted": match_data_wanted})
