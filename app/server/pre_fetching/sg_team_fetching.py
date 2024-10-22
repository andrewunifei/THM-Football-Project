import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.sg_team_statistics import SGTeamStatistics

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
            data = {}
            for info in record['statistics']:
                data[info['type']] = info['value']
            for record in statistics_data:
                new_statistic = SGTeamStatistics(
                    game_id=id,
                    team_id=record['team']['id'],
                    shots_on_goal=data["Shots on Goal"]['value'],
                    shots_off_goal=data["Shots off Goal"]['value'],
                    total_shots=data["Total Shots"]['value'],
                    blocked_shots=data["Blocked Shots"]['value'],
                    shots_insidebox=data["Shots insidebox",]['value'],
                    shots_outsidebox=data["Shots outsidebox"]['value'],
                    fouls=data["Fouls"]['value'],
                    corner_kicks=data["Corner Kicks"]['value'],
                    offsides=data["Offsides"]['value'],
                    yellow_cards=data["Yellow Cards"]['value'],
                    red_cards=data["Red Cards"]['value'],
                    goalkeeper_saves=data["Goalkeeper Saves"]['value'],
                    total_passes=data["Total passes"]['value'],
                    passes_accurate=data["Passes accurate"]['value'],
                    ball_possession=data["Ball Possession"]['value'],  # Ensure this is a decimal value
                    passes_percentage=data["Passes %"]['value'],  # Ensure this is a decimal value
                )
                session.add(new_statistic)  # Add new statistic record to the session

            # Step 5: Commit the session
            session.commit()
            print('Data inserted successfully.')

        else:
            print(f'Failed to fetch data from API: {response.status_code}')