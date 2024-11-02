import requests
from sqlalchemy import create_engine
from models.injury import Injury

def get_players_ids():
    url = 'http://127.0.0.1:5000/players-id'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return []

def get_games_ids():
    url = 'http://127.0.0.1:5000/games-id'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return []

def fetch_injury_and_populate(api_key, league, season, db_session):
    players_ids = get_players_ids()
    games_ids = get_games_ids()
    if((len(players_ids) == 0) or (len(games_ids) == 0)):
        return

    injuries_endpoint = f'injuries?league={league}&season={season}'
    api_url = f'https://v3.football.api-sports.io/{injuries_endpoint}'
    headers = {
        'x-rapidapi-host': 'v3.football.api-sports.io',
        'x-rapidapi-key': api_key
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        injuries_data = response.json()    
        injuries_data = injuries_data['response']

        for injury in injuries_data:
            validation_flag1 = (int(injury['player']['id']) in players_ids)
            validation_flag2 = (int(injury['fixture']['id']) in games_ids)
            if(validation_flag1 and validation_flag2):
                new_injury = Injury(
                    player_id=injury['player']['id'],
                    game_id=injury['fixture']['id'],
                    type=injury['player']['type'],
                    reason=injury['player']['reason']
                )
                db_session.add(new_injury)  
            else:
                continue

        db_session.commit()
        print('Data inserted successfully.')

    else:
        print(f'Failed to fetch data from API: {response.status_code}')