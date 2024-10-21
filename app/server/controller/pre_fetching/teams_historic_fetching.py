import json
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import TeamsHistoric

def get_players_id():
    data = []
    with open('players_id.json', 'r') as file:
        data = json.load(file)
    return data

def fetch_venue_and_populate(api_key, session): 
    players_ids = get_players_id()

    for id in players_ids:
        api_url = f'https://v3.football.api-sports.io/players/teams?player={id}'
        headers = {
            'x-rapidapi-host': 'v3.football.api-sports.io',
            'x-rapidapi-key': api_key
        }
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            teams_historic_data = response.json()
            for record in teams_historic_data:
                new_record = TeamsHistoric(
                    player_id=id,   
                    team_id=record['response']['team']['id'],
                    seasons=record['response']['seasons']
                )
                session.add(new_record)

            session.commit()
            print("Data inserted successfully.")

        else:
            print(f"Failed to fetch data from API: {response.status_code}")