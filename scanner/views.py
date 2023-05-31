import json

import numpy as np
from django.http import JsonResponse
from django.shortcuts import render

from teams.models import Teams, Team_Match_Data


def scanner(request):
    # Receive fetch from scanner.js
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data_from_post = json.load(request)

        # Retrieve team number and grids from QR data
        team_number = int(data_from_post["teamNumber"])
        auto_grid_list = np.array(json.loads(data_from_post["autoGrid"]))
        teleop_grid_list = np.array(json.loads(data_from_post["teleGrid"]))
        total_points = points_calculator(data_from_post, auto_grid_list, teleop_grid_list)

        # Either retrieves Team object or creates a new one
        team_object, created = Teams.objects.get_or_create(team_number=team_number)

        # Creates a new Team_Match_Data with given data if it doesn't exist
        Team_Match_Data.objects.get_or_create(
            team=team_object,
            match_number=data_from_post["matchNumber"],
            auto_charging_station=data_from_post["autoChargingStation"],
            auto_upper=auto_grid_list[0],
            auto_upper_counts=np.count_nonzero(auto_grid_list[0]),
            auto_middle=auto_grid_list[1],
            auto_middle_counts=np.count_nonzero(auto_grid_list[1]),
            auto_lower=auto_grid_list[2],
            auto_lower_counts=np.count_nonzero(auto_grid_list[2]),
            teleop_upper=teleop_grid_list[0],
            teleop_upper_counts=np.count_nonzero(teleop_grid_list[0]),
            teleop_middle=teleop_grid_list[1],
            teleop_middle_counts=np.count_nonzero(teleop_grid_list[1]),
            teleop_lower=teleop_grid_list[2],
            teleop_lower_counts=np.count_nonzero(teleop_grid_list[2]),
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


def points_calculator(json_data, auto_grid_list, teleop_grid_list):
    # Specified point values from Game Manuel
    AUTO_CHARGING_STATION_POINTS = np.array([0, 3, 8, 12])
    END_CHARGING_STATION_POINTS = np.array([0, 2, 6, 10])
    AUTO_GRID_POINTS = np.array([[6], [4], [3]])
    TELEOP_GRID_POINTS = np.array([[5], [3], [2]])

    # Returns number of non-zero values on each row in a 3x1 matrix
    auto_grid_counts = np.count_nonzero(auto_grid_list, axis=1, keepdims=True)
    teleop_grid_counts = np.count_nonzero(teleop_grid_list, axis=1, keepdims=True)

    # Vector multiplication between counts and points
    auto_grid_points = np.sum(auto_grid_counts * AUTO_GRID_POINTS)
    teleop_grid_points = np.sum(teleop_grid_counts * TELEOP_GRID_POINTS)

    auto_charging_station_points = AUTO_CHARGING_STATION_POINTS[int(json_data["autoChargingStation"])]
    end_charging_station_points = END_CHARGING_STATION_POINTS[int(json_data["endChargingStation"])]

    return auto_grid_points + teleop_grid_points + auto_charging_station_points + end_charging_station_points
