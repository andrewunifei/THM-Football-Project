import requests
import time
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models.player import Player

def call_api(api_key, endpoint, params=None):
    if params is None:
        params = {}

    url = f'https://v3.football.api-sports.io/{endpoint}'
    headers = {
        'x-rapidapi-host': 'v3.football.api-sports.io',
        'x-rapidapi-key': api_key
    }
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()  
    else:
        response.raise_for_status() 

# Função recursiva por conta do sistema de paginação desse enpoint da API
def generate_players_data(api_key, league, season, page=1, players_data=None):
    if players_data is None:
        players_data = []

    players = call_api(api_key, 'players', {'league': league, 'season': season, 'page': page})
    players_data.extend(players['response'])

    if players['paging']['current'] < players['paging']['total']:
        page = players['paging']['current'] + 1
        
        if page % 2 == 1:
            time.sleep(1) # Pra evitar 429 - Too Many Requests

        players_data = generate_players_data(league, season, page, players_data)

    return players_data

# Esses dados são referentes a entidade 'Jogadr' no diagrama ER
def fetch_player_and_populate(api_key, league, season, db_session):
    players_data = generate_players_data(api_key, league, season)
    players_id = []

    for player in players_data:
        players_id.append(player['player']['player_id']) # Agregar para escrever em um arquivo
        new_player = Player(
            player_id=player['player']['player_id'],
            name=player['player']['name'],
            first_name=player['player']['firstname'],
            last_name=player['player']['lastname'],
            age=player['player']['age'],
            position=player['statistics']['games']['position'],
            birth=player['player']['birth'],  # JSON object
            nationality=player['player']['nationality'],
            height=player['player']['height'],
            weight=player['player']['weight'],
            injured=player['player']['injured'],
            photo=player['player']['photo'],
            games_appearances=player['statistics']['games']['appearances'],
            games_lineups=player['statistics']['games']['lineups'],
            minutes_played_total=player['statistics']['games']['minutes'],
            rating=player['statistics']['games']['rating'],
            substitutes_in=player['statistics']['substitutes']['in'],
            substitutes_out=player['statistics']['substitutes']['out'],
            bench=player['statistics']['substitutes']['bench'],
            shots_on=player['statistics']['shots']['on'],
            shots_total=player['statistics']['shots']['total'],
            goals_total=player['statistics']['goals']['total'],
            goals_conceded=player['statistics']['goals']['conceded'],
            goals_assists=player['statistics']['goals']['assists'],
            goals_saved=player['statistics']['goals']['saves'],
            passes_total=player['statistics']['passes']['total'],
            passes_key=player['statistics']['passes']['key'],
            passes_accuracy=player['statistics']['passes']['accuracy'], 
            tackles_total=player['statistics']['tackles']['total'],
            tackles_blocks=player['statistics']['tackles']['blocks'],
            tackles_interceptions=player['statistics']['tackles']['interceptions'],
            duels_total=player['statistics']['duels']['total'],
            duels_won_total=player['statistics']['duels']['won'],
            dribbles_attempts_total=player['statistics']['dribbles']['attempts'],
            dribbles_success_total=player['statistics']['dribbles']['success'],
            dribbles_past_total=player['statistics']['dribbles']['past'],
            fouls_drawn_total=player['statistics']['fouls']['drawn'],
            fouls_committed_total=player['statistics']['fouls']['committed'],
            cards_yellow_total=player['statistics']['cards']['yellow'], 
            cards_red_total=player['statistics']['cards']['red'], 
            penalty_won_total=player['statistics']['penalty']['won'], 
            penalty_committed_total=player['statistics']['penalty']['committed'], 
            penalty_scored_total=player['statistics']['penalty']['scored'], 
            penalty_missed_total=player['statistics']['penalty']['missed'], 
            penalty_saved_total=player['statistics']['penalty']['saved'], 
            team_id=player['statistics']['team']['id']
        )
        session.add(new_player)

    with open('players_id.json', 'w') as file:
        json.dump(players_id, file) # Irei usar esses ids para capturar dados em teams_historic_fetching

    session.commit()
    print("Data inserted successfully.")