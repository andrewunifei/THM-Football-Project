import requests
import time
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.player import Player

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

def get_teams_ids():
    url = 'http://127.0.0.1:5000/teams/ids'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return []

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

        players_data = generate_players_data(api_key, league, season, page, players_data)

    return players_data

# Esses dados são referentes a entidade 'Jogadr' no diagrama ER
def fetch_player_and_populate(api_key, league, season, db_session):
    teams_ids = get_teams_ids()
    if(len(teams_ids) == 0):
        return

    players_data = generate_players_data(api_key, league, season)
    players_id = []

    for player in players_data:
        players_id.append(player['player']['id']) # Agregar para escrever em um arquivo
        if(int(player['statistics'][0]['team']['id']) in teams_ids):
            new_player = Player(
                player_id=player['player']['id'],
                name=player['player']['name'],
                first_name=player['player']['firstname'],
                last_name=player['player']['lastname'],
                age=player['player']['age'],
                position=player['statistics'][0]['games']['position'],
                birth=player['player']['birth'],  # JSON object
                nationality=player['player']['nationality'],
                height=player['player']['height'],
                weight=player['player']['weight'],
                injured=player['player']['injured'],
                photo=player['player']['photo'],
                games_appearences=player['statistics'][0]['games']['appearences'],
                games_lineups=player['statistics'][0]['games']['lineups'],
                minutes_played_total=player['statistics'][0]['games']['minutes'],
                rating=player['statistics'][0]['games']['rating'],
                substitutes_in=player['statistics'][0]['substitutes']['in'],
                substitutes_out=player['statistics'][0]['substitutes']['out'],
                bench=player['statistics'][0]['substitutes']['bench'],
                shots_on=player['statistics'][0]['shots']['on'],
                shots_total=player['statistics'][0]['shots']['total'],
                goals_total=player['statistics'][0]['goals']['total'],
                goals_conceded=player['statistics'][0]['goals']['conceded'],
                goals_assists=player['statistics'][0]['goals']['assists'],
                goals_saved=player['statistics'][0]['goals']['saves'],
                passes_total=player['statistics'][0]['passes']['total'],
                passes_key=player['statistics'][0]['passes']['key'],
                passes_accuracy=player['statistics'][0]['passes']['accuracy'], 
                tackles_total=player['statistics'][0]['tackles']['total'],
                tackles_blocks=player['statistics'][0]['tackles']['blocks'],
                tackles_interceptions=player['statistics'][0]['tackles']['interceptions'],
                duels_total=player['statistics'][0]['duels']['total'],
                duels_won_total=player['statistics'][0]['duels']['won'],
                dribbles_attempts_total=player['statistics'][0]['dribbles']['attempts'],
                dribbles_success_total=player['statistics'][0]['dribbles']['success'],
                dribbles_past_total=player['statistics'][0]['dribbles']['past'],
                fouls_drawn_total=player['statistics'][0]['fouls']['drawn'],
                fouls_committed_total=player['statistics'][0]['fouls']['committed'],
                cards_yellow_total=player['statistics'][0]['cards']['yellow'], 
                cards_red_total=player['statistics'][0]['cards']['red'], 
                penalty_won_total=player['statistics'][0]['penalty']['won'], 
                penalty_committed_total=player['statistics'][0]['penalty']['commited'], 
                penalty_scored_total=player['statistics'][0]['penalty']['scored'], 
                penalty_missed_total=player['statistics'][0]['penalty']['missed'], 
                penalty_saved_total=player['statistics'][0]['penalty']['saved'], 
                team_id=player['statistics'][0]['team']['id']
            )
            db_session.add(new_player)
        else:
            continue

    with open('players_id.json', 'w') as file:
        json.dump(players_id, file) # Irei usar esses ids para capturar dados em teams_historic_fetching

    db_session.commit()
    print('Data inserted successfully.')