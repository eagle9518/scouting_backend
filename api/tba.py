import requests

team_key = "frc2073"
year = 2024
X_TBA_Auth_Key = "opXlAfkuD4tQbDm2iskpBHdyYQbarWsQoeSG8w6MSKQ0c8jtbOnbREQu7z7nfUCK"
event_key = "2023azgl"


def get_team_events():
    team_events = requests.get(f"https://www.thebluealliance.com/api/v3/team/{team_key}/events/{year}",
                               headers={"X-TBA-Auth-Key": X_TBA_Auth_Key})

    events = {}
    for event in team_events.json():
        events[event["key"]] = event["short_name"]
    events["testing"] = "Training"

    return events


def get_match_schedule():
    matches_at_event = requests.get(f"https://www.thebluealliance.com/api/v3/event/{event_key}/matches/simple",
                                    headers={"X-TBA-Auth-Key": X_TBA_Auth_Key}).json()
    return matches_at_event


def get_teams_list():
    teams_at_event = requests.get(f"https://www.thebluealliance.com/api/v3/event/{event_key}/teams/simple",
                                  headers={"X-TBA-Auth-Key": X_TBA_Auth_Key}).json()
    return teams_at_event


def get_single_match(match_id):
    match_key = event_key + "_" + match_id
    raw_match = requests.get(f"https://www.thebluealliance.com/api/v3/match/{match_key}/simple",
                             headers={"X-TBA-Auth-Key": X_TBA_Auth_Key}).json()

    match = {"red": [], "blue": []}
    for red_team in raw_match["alliances"]["red"]["team_keys"]:
        match["red"].append(red_team.split("frc")[1])
    for blue_team in raw_match["alliances"]["blue"]["team_keys"]:
        match["blue"].append(blue_team.split("frc")[1])

    return match
