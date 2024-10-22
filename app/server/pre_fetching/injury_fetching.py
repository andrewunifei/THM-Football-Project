import requests
from sqlalchemy import create_engine
from .models.injury import Injury

def fetch_injury_and_populate(api_key, db_session, league, season):
    injuries_endpoint = f'injuries?league={league}&season={season}'
    api_url = f'https://v3.football.api-sports.io/{injuries_endpoint}'
    headers = {
        'x-rapidapi-host': 'v3.football.api-sports.io',
        'x-rapidapi-key': api_key
    }
    response = requests.get(url)

    if response.status_code == 200:
        injuries_data = response.json()    
        injuries_data = injuries_data['response']

        for injury in injuries_data:
            new_injury = Injuries(
                player_id=injury['player']['id'],
                game_id=injury['fixture']['id'],
                type=injury['player']['type'],
                reason=injury['player']['reason']
            )
            db_session.add(new_injury)  
            
        db_session.commit()
        print("Data inserted successfully.")

    else:
        print(f"Failed to fetch data from API: {response.status_code}")