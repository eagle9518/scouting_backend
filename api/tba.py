import requests

team_key = "frc2073"
year = 2023
X_TBA_Auth_Key = "opXlAfkuD4tQbDm2iskpBHdyYQbarWsQoeSG8w6MSKQ0c8jtbOnbREQu7z7nfUCK"
event_key = "2023azva"


def get_team_events():
    team_events = requests.get(f"https://www.thebluealliance.com/api/v3/team/{team_key}/events/{year}/keys",
                               headers={"X-TBA-Auth-Key": X_TBA_Auth_Key}).json()
    return team_events


def get_match_schedule():
    matches_at_event = requests.get(f"https://www.thebluealliance.com/api/v3/event/{event_key}/matches/simple",
                                    headers={"X-TBA-Auth-Key": X_TBA_Auth_Key}).json()
    return matches_at_event


def get_teams_list():
    teams_at_event = requests.get(f"https://www.thebluealliance.com/api/v3/event/{event_key}/teams/simple",
                                  headers={"X-TBA-Auth-Key": X_TBA_Auth_Key}).json()
    return teams_at_event



