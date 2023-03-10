import json

import numpy as np
from django.http import JsonResponse
from django.shortcuts import render
from teams.models import Teams, Team_Match_Data
from matches.models import Matches
from numpy import count_nonzero

# Create your views here.
AUTO_CHARGING_STATION = [0, 3, 8, 12]
END_CHARGING_STATION = [0, 2, 6, 10]


def scanner(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data_from_post = json.load(request)
        total_points = points_calculator(data_from_post)

        team_number = int(data_from_post["teamNumber"])
        if not Teams.objects.filter(team_number=team_number).exists():
            team_object = Teams.objects.create(team_number=team_number)
        else:
            team_object = Teams.objects.get(team_number=team_number)

        auto_grid_list = json.loads(data_from_post["autoGrid"])
        teleop_grid_list = json.loads(data_from_post["teleGrid"])

        if not Team_Match_Data.objects.filter(team=team_object, match_number=data_from_post["matchNumber"]).exists():
            Team_Match_Data.objects.create(
                team=team_object,
                match_number=data_from_post["matchNumber"],
                auto_charging_station=data_from_post["autoChargingStation"],
                auto_upper=auto_grid_list[0],
                auto_upper_counts=int(count_nonzero(auto_grid_list[0])),
                auto_middle=auto_grid_list[1],
                auto_middle_counts=int(count_nonzero(auto_grid_list[1])),
                auto_lower=auto_grid_list[2],
                auto_lower_counts=int(count_nonzero(auto_grid_list[2])),
                teleop_upper=teleop_grid_list[0],
                teleop_upper_counts=int(count_nonzero(teleop_grid_list[0])),
                teleop_middle=teleop_grid_list[1],
                teleop_middle_counts=int(count_nonzero(teleop_grid_list[1])),
                teleop_lower=teleop_grid_list[2],
                teleop_lower_counts=int(count_nonzero(teleop_grid_list[2])),
                cone_transport=data_from_post["coneTransport"],
                cube_transport=data_from_post["cubeTransport"],
                end_charging_station=data_from_post["endChargingStation"],
                total_points=total_points,
                driver_ranking=data_from_post["driverRanking"],
                defense_ranking=data_from_post["defenseRanking"],
                comment=data_from_post["comment"],
                scout_name=data_from_post["name"],
            )

        response = {"confirmation": "Successfully Sent"}
        return JsonResponse(response)

    return render(request, 'qr_scanner.html')


def points_calculator(json_data):
    auto_grid_list = json.loads(json_data["autoGrid"])
    auto_top_points = count_nonzero(auto_grid_list[0]) * 6
    auto_middle_points = count_nonzero(auto_grid_list[1]) * 4
    auto_bottom_points = count_nonzero(auto_grid_list[2]) * 3

    teleop_grid_list = json.loads(json_data["teleGrid"])
    teleop_top_points = count_nonzero(teleop_grid_list[0]) * 5
    teleop_middle_points = count_nonzero(teleop_grid_list[1]) * 3
    teleop_bottom_points = count_nonzero(teleop_grid_list[2]) * 2

    auto_charging_station_points = AUTO_CHARGING_STATION[int(json_data["autoChargingStation"])]
    end_charging_station_points = END_CHARGING_STATION[int(json_data["endChargingStation"])]

    return auto_top_points + auto_middle_points + auto_bottom_points + \
           teleop_top_points + teleop_middle_points + teleop_bottom_points + \
           auto_charging_station_points + end_charging_station_points
