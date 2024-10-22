import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models.sg_player_statistics import SGPlayerStatistics

def get_games_id():
    data = []
    with open('games_id.json', 'r') as file:
        data = json.load(file)
    return data

def fetch_sg_player_and_populate(api_key, db_session):
    games_id = get_games_id()

    for id in games_id:
        # TODO: Handle null values

        sg_player_statistics_endpoint = f'fixtures/players/fixture={id}'
        api_url = f'https://v3.football.api-sports.io/{sg_team_player_endpoint}'
        headers = {
            'x-rapidapi-host': 'v3.football.api-sports.io',
            'x-rapidapi-key': api_key
        }
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            player_statistics_data = response.json()
            player_statistics_data = player_statistics_data['response']

            # Step 4: Insert data into the database
            for record in player_statistics_data:
                new_statistic = SGPlayerStatistics(
                    player_id=record['player']['id'],          # Adjust based on your API response structure
                    game_id=id,
                    player_number=record['statistics']['games']['number'],
                    position=record['statistics']['games']['position'],
                    rating=record['statistics']['games']['rating'], # Provavelmente precisa de ajusta já que o retonro é uma string e essa variável espera um decimal
                    captain=record['statistics']['games']['captain'],
                    substitute=record['statistics']['games']['substitute'],
                    offsides=record['statistics']['offsides'],
                    shots_on=record['statistics']['shots']['on'],
                    shots_total=record['statistics']['shots']['total'],
                    goals_total=record['statistics']['goals']['total'],
                    goals_conceded=record['statistics']['goals']['conceded'],
                    goals_assists=record['statistics']['goals']['assists'],
                    goals_saves=record['statistics']['goals']['saves'],
                    passes_total=record['statistics']['passes']['total'],
                    passes_key=record['statistics']['passes']['key'],
                    passes_accuracy=record['statistics']['passes']['accuracy'],  # Ensure this is a decimal value
                    tackles_total=record['statistics']['tackles']['total'],
                    tackles_blocks=record['statistics']['tackles']['blocks'], # Verificar o nome dessa variável no modelo
                    tackles_interceptions=record['statistics']['tackles']['interceptions'],  # Verificar o nome dessa variável no modelo
                    duels_total=record['statistics']['duels']['total'],
                    duels_won=record['statistics']['duels']['won'],
                    dribbles_attempts=record['statistics']['dribbles']['attempts'],
                    dribbles_success=record['statistics']['dribbles']['success'],
                    dribbles_past=record['statistics']['dribbles']['past'],
                    fouls_drawn=record['statistics']['fouls']['drawn'],
                    fouls_committed=record['statistics']['fouls']['committed'],
                    yellow_cards=record['statistics']['cards']['yellow'],
                    red_cards=record['statistics']['cards']['red'],
                    penalty_won=record['statistics']['penalty']['won'],
                    penalty_committed=record['statistics']['penalty']['committed'],
                    penalty_scored=record['statistics']['penalty']['scored'],
                    penalty_missed=record['statistics']['penalty']['missed'],
                    penalty_saved=record['statistics']['penalty']['saved']
                )
                db_session.add(new_statistic)  # Add new statistic record to the db_session

            # Step 5: Commit the db_session
            db_session.commit()
            print('Data inserted successfully.')

        else:
            print(f'Failed to fetch data from API: {response.status_code}')