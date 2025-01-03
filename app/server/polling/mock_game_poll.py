import requests
from sqlalchemy import create_engine
from models.game import Game
import json

def get_teams_ids():
    url = 'http://127.0.0.1:5000/teams/ids'
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
    url = 'http://127.0.0.1:5000/stadiums/venues-ids'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return []

def handle_polling_game(api_url, db_session, api_key):
    teams_ids = get_teams_ids()
    venues_ids = get_venues_ids()
    new_games_ids = []

    if((len(teams_ids) == 0) or (len(venues_ids) == 0)):
        return
    
    headers = {
        'x-rapidapi-host': 'v3.football.api-sports.io',
        'x-rapidapi-key': api_key
    }
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        games_data = response.json()
        games_data = games_data['response']
        
        if(len(games_data) > 0):
            for game in games_data:
                winner = ''
                if game['teams']['home']['winner'] == 'true':
                    winner = game['teams']['home']['id']
                else:
                    winner = game['teams']['away']['id']

                new_game = Game(
                    game_id=game['fixture']['id'],
                    referee=game['fixture']['referee'],
                    timezone=game['fixture']['timezone'],
                    date=game['fixture']['date'],
                    first_period=game['fixture']['periods']['first'],
                    second_period=game['fixture']['periods']['second'],
                    score=game['score'],
                    home_team_goals=game['goals']['home'],
                    away_team_goals=game['goals']['away'],
                    venue_id=game['fixture']['venue']['id'], 
                    home_team_id=game['teams']['home']['id'], 
                    away_team_id=game['teams']['away']['id'],
                    winner_team_id=winner
                )
                db_session.add(new_game)
                print('Data added successfully.')
                new_games_ids.append([game['teams']['home']['id'], game['teams']['away']['id']])

            db_session.commit()
            print('Commited successfully.')

            return new_games_ids
        else:
            return []

    else:
        print(f'Failed to fetch data from API: {response.status_code}')