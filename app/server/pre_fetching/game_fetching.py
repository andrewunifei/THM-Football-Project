import requests
from sqlalchemy import create_engine
from models.game import Game
import json

def get_teams_ids():
    url = 'http://127.0.0.1:5000/teams-id'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return []

def get_venues_ids():
    url = 'http://127.0.0.1:5000/venues-id'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return []

def fetch_game_and_populate(api_key, league, season, db_session):
    teams_ids = get_teams_ids()
    venues_ids = get_venues_ids()
    if((len(teams_ids) == 0) or (len(venues_ids) == 0)):
        return
    
    fixture_endpoint = f'fixtures?league={league}&season={season}'
    api_url = f'https://v3.football.api-sports.io/{fixture_endpoint}'
    headers = {
        'x-rapidapi-host': 'v3.football.api-sports.io',
        'x-rapidapi-key': api_key
    }
    response = requests.get(api_url, headers=headers)
    games_data = response.json()
    games_data = games_data['response']

    if response.status_code == 200:
        games_id = []
        for game in games_data:
            winner = ''
            games_id.append(game['fixture']['id'])
            if game['teams']['home']['winner'] == 'true':
                winner = game['teams']['home']['id']
            else:
                winner = game['teams']['away']['id']

            validation_flag1 = (
                int(winner) in teams_ids and
                int(game['teams']['home']['id']) in teams_ids and
                int(game['teams']['away']['id']) in teams_ids
            )
            validation_flag2 = (int(game['fixture']['venue']['id']) in venues_ids)

            if(validation_flag1 and validation_flag2):
                new_game = Game(
                    game_id=game['fixture']['id'],
                    referee=game['fixture']['referee'],
                    timezone=game['fixture']['timezone'],
                    date=game['fixture']['date'],
                    first_period=game['fixture']['periods']['first'],
                    second_period=game['fixture']['periods']['second'],
                    score=game['score'],  # JSON object
                    home_team_goals=game['goals']['home'],
                    away_team_goals=game['goals']['away'],
                    venue_id=game['fixture']['venue']['id'],  # Foreign key reference to Venue
                    home_team_id=game['teams']['home']['id'],  # Foreign key reference to Team
                    away_team_id=game['teams']['away']['id'],  # Foreign key reference to Team
                    winner_team_id=winner
                )
                db_session.add(new_game)
            else:
                continue

        with open('games_id.json', 'w') as file:
            json.dump(games_id, file) # Irei usar esses ids para capturar dados em sg_team_fetching e sg_player_fetching

        db_session.commit()
        print('Data inserted successfully.')

    else:
        print(f'Failed to fetch data from API: {response.status_code}')