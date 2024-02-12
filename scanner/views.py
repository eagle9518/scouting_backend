import json

import numpy as np
from django.http import JsonResponse
from django.shortcuts import render

from teams.models import Teams, Team_Match_Data


def scanner(request):
    # Receive fetch from scanner.js
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data_from_post = json.load(request)

        # Creates a new Team_Match_Data with given data if it doesn't exist
        Team_Match_Data.objects.create(team=int(data_from_post["teamNumber"]),
                                       event=data_from_post["compCode"],
                                       match_number=data_from_post["matchNumber"],
                                       quantifier='Quals',

                                       auto_leave=data_from_post["autoLeave"],
                                       auto_amp=data_from_post["autoAmp"],
                                       auto_speaker_make=data_from_post["autoSpeakerMake"],
                                       auto_speaker_miss=data_from_post["autoSpeakerMiss"],

                                       teleop_amp=data_from_post["teleopAmp"],
                                       teleop_speaker_make=data_from_post["teleopSpeakerMake"],
                                       teleop_speaker_miss=data_from_post["teleopSpeakerMiss"],

                                       trap=data_from_post["trapNumber"],
                                       climb=data_from_post["endClimb"],

                                       driver_ranking=data_from_post["driverRanking"],
                                       defense_ranking=data_from_post["defenseRanking"],
                                       comment=data_from_post["comment"],
                                       scout_name=data_from_post["name"])

        response = {"confirmation": "Successfully Sent"}
        return JsonResponse(response)

    return render(request, 'qr_scanner.html')


# def points_calculator(json_data, auto_grid_list, teleop_grid_list):
#     # Specified point values from Game Manuel
#     AUTO_CHARGING_STATION_POINTS = np.array([0, 3, 8, 12])
#     END_CHARGING_STATION_POINTS = np.array([0, 2, 6, 10])
#     AUTO_GRID_POINTS = np.array([[6], [4], [3]])
#     TELEOP_GRID_POINTS = np.array([[5], [3], [2]])
#
#     # Returns number of non-zero values on each row in a 3x1 matrix
#     auto_grid_counts = np.count_nonzero(auto_grid_list, axis=1, keepdims=True)
#     teleop_grid_counts = np.count_nonzero(teleop_grid_list, axis=1, keepdims=True)
#
#     # Vector multiplication between counts and points
#     auto_grid_points = np.sum(auto_grid_counts * AUTO_GRID_POINTS)
#     teleop_grid_points = np.sum(teleop_grid_counts * TELEOP_GRID_POINTS)
#
#     auto_charging_station_points = AUTO_CHARGING_STATION_POINTS[int(json_data["autoChargingStation"])]
#     end_charging_station_points = END_CHARGING_STATION_POINTS[int(json_data["endChargingStation"])]
#
#     return auto_grid_points + teleop_grid_points + auto_charging_station_points + end_charging_station_points
