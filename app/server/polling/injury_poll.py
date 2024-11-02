import requests
from sqlalchemy import create_engine
from models.injury import Injury

def handle_polling_injury(api_key, league, season, game_id, db_session):
    injuries_endpoint = f'injuries?league={league}&season={season}&fixture={game_id}'
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
            new_injury = Injury(
                player_id=injury['player']['id'],
                game_id=injury['fixture']['id'],
                type=injury['player']['type'],
                reason=injury['player']['reason']
            )
            db_session.add(new_injury)  

        db_session.commit()
        print('Novos dados de lesão inseridos com sucesso.')

    else:
        print(f'Erro ao se comunicar com API com código: {response.status_code}')