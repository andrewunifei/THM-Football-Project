import requests
from sqlalchemy import create_engine
from ..models.game import Game

def fetch_game_and_populate(api_key, db_session):
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

            new_game = Game(
                game_id=game['fixture']['id'],
                referee=game['fixture']['referee'],
                timezone=game['fixture']['timezone'],
                date=game['fixture']['date'],
                first_period=game['periods']['first'],
                second_period=game['periods']['second'],
                score=game['score'],  # JSON object
                home_team_goals=game['goals']['home'],
                away_team_goals=game['goals']['away'],
                venue_id=game['fixture']['venue']['id'],  # Foreign key reference to Venue
                home_team_id=game['teams']['home']['id'],  # Foreign key reference to Team
                away_team_id=game['teams']['away']['id'],  # Foreign key reference to Team
                winner_team_id=winner
            )
            db_session.add(new_game)

        with open('games_id.json', 'w') as file:
            json.dump(games_id, file) # Irei usar esses ids para capturar dados em sg_team_fetching e sg_player_fetching

        db_session.commit()
        print("Data inserted successfully.")

    else:
        print(f"Failed to fetch data from API: {response.status_code}")