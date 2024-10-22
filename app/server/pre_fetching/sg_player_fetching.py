import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.sg_player_statistics import SGPlayerStatistics

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
                    player_id=record['players']['player']['id'],          # Adjust based on your API response structure
                    game_id=id,
                    player_number=record['players']['statistics'][0]['games']['number'],
                    position=record['players']['statistics'][0]['games']['position'],
                    rating=record['players']['statistics'][0]['games']['rating'], # Provavelmente precisa de ajustar já que o retonro é uma string e essa variável espera um decimal
                    captain=record['players']['statistics'][0]['games']['captain'],
                    substitute=record['players']['statistics'][0]['games']['substitute'],
                    offsides=record['players']['statistics'][0]['offsides'],
                    shots_on=record['players']['statistics'][0]['shots']['on'],
                    shots_total=record['players']['statistics'][0]['shots']['total'],
                    goals_total=record['players']['statistics'][0]['goals']['total'],
                    goals_conceded=record['players']['statistics'][0]['goals']['conceded'],
                    goals_assists=record['players']['statistics'][0]['goals']['assists'],
                    goals_saves=record['players']['statistics'][0]['goals']['saves'],
                    passes_total=record['players']['statistics'][0]['passes']['total'],
                    passes_key=record['players']['statistics'][0]['passes']['key'],
                    passes_accuracy=record['players']['statistics'][0]['passes']['accuracy'],  # Ensure this is a decimal value
                    tackles_total=record['players']['statistics'][0]['tackles']['total'],
                    tackles_blocks=record['players']['statistics'][0]['tackles']['blocks'], # Verificar o nome dessa variável no modelo
                    tackles_interceptions=record['players']['statistics'][0]['tackles']['interceptions'],  # Verificar o nome dessa variável no modelo
                    duels_total=record['players']['statistics'][0]['duels']['total'],
                    duels_won=record['players']['statistics'][0]['duels']['won'],
                    dribbles_attempts=record['players']['statistics'][0]['dribbles']['attempts'],
                    dribbles_success=record['players']['statistics'][0]['dribbles']['success'],
                    dribbles_past=record['players']['statistics'][0]['dribbles']['past'],
                    fouls_drawn=record['players']['statistics'][0]['fouls']['drawn'],
                    fouls_committed=record['players']['statistics'][0]['fouls']['committed'],
                    yellow_cards=record['players']['statistics'][0]['cards']['yellow'],
                    red_cards=record['players']['statistics'][0]['cards']['red'],
                    penalty_won=record['players']['statistics'][0]['penalty']['won'],
                    penalty_committed=record['players']['statistics'][0]['penalty']['committed'],
                    penalty_scored=record['players']['statistics'][0]['penalty']['scored'],
                    penalty_missed=record['players']['statistics'][0]['penalty']['missed'],
                    penalty_saved=record['players']['statistics'][0]['penalty']['saved']
                )
                db_session.add(new_statistic)  # Add new statistic record to the db_session

            # Step 5: Commit the db_session
            db_session.commit()
            print('Data inserted successfully.')

        else:
            print(f'Failed to fetch data from API: {response.status_code}')