import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models.sg_team_statistics import SGTeamStatistics

def get_games_id():
    data = []
    with open('games_id.json', 'r') as file:
        data = json.load(file)
    return data

def fetch_sg_team_and_populate():
    games_id = get_games_id()

    for id in games_id:
        sg_team_statistics_endpoint = f'fixtures/statistics/fixture={id}'
        api_url = f'https://v3.football.api-sports.io/{sg_team_statistics_endpoint}'
        headers = {
            'x-rapidapi-host': 'v3.football.api-sports.io',
            'x-rapidapi-key': api_key
        }
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            statistics_data = response.json()
            statistics_data = statistics_data['response']

            for record in statistics_data:
                new_statistic = SGTeamStatistics(
                    game_id=id,
                    team_id=record['team']['id'],
                    shots_on_goal=record['statistics'][0]['value'],
                    shots_off_goal=record['statistics'][1]['value'],
                    total_shots=record['statistics'][2]['value'],
                    blocked_shots=record['statistics'][3]['value'],
                    shots_insidebox=record['statistics'][4]['value'],
                    shots_outsidebox=record['statistics'][5]['value'],
                    fouls=record['statistics'][6]['value'],
                    corner_kicks=record['statistics'][7]['value'],
                    offsides=record['statistics'][8]['value'],
                    yellow_cards=record['statistics'][9]['value'],
                    red_cards=record['statistics'][10]['value'],
                    goalkeeper_saves=record['statistics'][11]['value'],
                    total_passes=record['statistics'][12]['value'],
                    passes_accurate=record['statistics'][13]['value'],
                    ball_possession=record['statistics'][14]['value'],  # Ensure this is a decimal value
                    passes_percentage=record['statistics'][15]['value'],  # Ensure this is a decimal value
                    expected_goals=record['statistics'][16]['value']   # Ensure this is a decimal value
                )
                session.add(new_statistic)  # Add new statistic record to the session

            # Step 5: Commit the session
            session.commit()
            print('Data inserted successfully.')

        else:
            print(f'Failed to fetch data from API: {response.status_code}')