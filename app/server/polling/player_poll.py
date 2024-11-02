from sqlalchemy import update
import requests
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

# Função recursiva por conta do sistema de paginação desse enpoint da API
def generate_players_data(api_key, league, season, page=1, players_data=None):
    if players_data is None:
        players_data = []

    players = call_api(
        api_key,
        'players',
        {'league': league, 'season': season, 'team': team_id, 'page': page}
    )
    players_data.extend(players['response'])

    if players['paging']['current'] < players['paging']['total']:
        page = players['paging']['current'] + 1
        
        if page % 2 == 1:
            time.sleep(1) # Pra evitar 429 - Too Many Requests

        players_data = generate_players_data(api_key, league, season, page, players_data)

    return players_data

def handle_polling_player(engine, db_session, api_key, league, season, team_id):
    all_columns = Team.__table__.c.keys()
    excluded_columns = {
        'player_id',
        'name',
        'first_name',
        'last_name',
        'age',
        'position', 
        'birth',
        'nationality', 
        'height',
        'weight',
        'injured',
        'photo',
        'team_id'
    }
    selected_columns = [col for col in all_columns if col not in excluded_columns]
    players_data = generate_players_data(api_key, league, seaso, team_id)

    for player in players_data:
        # O jogador já existe no banco de dados
        # Essa lógica é para atualizar apenas as novas informações depois de um novo jogo
        stmt = (
            update(Player)
            .where(Player.player_id == player_id)
            .values(**{
                selected_columns[0]:player['statistics'][0]['games']['appearences'],
                selected_columns[1]:player['statistics'][0]['games']['lineups'],
                selected_columns[2]:player['statistics'][0]['games']['minutes'],
                selected_columns[3]:player['statistics'][0]['games']['rating'],
                selected_columns[4]:player['statistics'][0]['substitutes']['in'],
                selected_columns[5]:player['statistics'][0]['substitutes']['out'],
                selected_columns[6]:player['statistics'][0]['substitutes']['bench'],
                selected_columns[7]:player['statistics'][0]['shots']['on'],
                selected_columns[8]:player['statistics'][0]['shots']['total'],
                selected_columns[9]:player['statistics'][0]['goals']['total'],
                selected_columns[10]:player['statistics'][0]['goals']['conceded'],
                selected_columns[11]:player['statistics'][0]['goals']['assists'],
                selected_columns[12]:player['statistics'][0]['goals']['saves'],
                selected_columns[13]:player['statistics'][0]['passes']['total'],
                selected_columns[14]:player['statistics'][0]['passes']['key'],
                selected_columns[15]:player['statistics'][0]['passes']['accuracy'], 
                selected_columns[16]:player['statistics'][0]['tackles']['total'],
                selected_columns[17]:player['statistics'][0]['tackles']['blocks'],
                selected_columns[18]:player['statistics'][0]['tackles']['interceptions'],
                selected_columns[19]:player['statistics'][0]['duels']['total'],
                selected_columns[20]:player['statistics'][0]['duels']['won'],
                selected_columns[21]:player['statistics'][0]['dribbles']['attempts'],
                selected_columns[22]:player['statistics'][0]['dribbles']['success'],
                selected_columns[23]:player['statistics'][0]['dribbles']['past'],
                selected_columns[24]:player['statistics'][0]['fouls']['drawn'],
                selected_columns[25]:player['statistics'][0]['fouls']['committed'],
                selected_columns[26]:player['statistics'][0]['cards']['yellow'], 
                selected_columns[27]:player['statistics'][0]['cards']['red'], 
                selected_columns[28]:player['statistics'][0]['penalty']['won'], 
                selected_columns[29]:player['statistics'][0]['penalty']['commited'], 
                selected_columns[30]:player['statistics'][0]['penalty']['scored'], 
                selected_columns[31]:player['statistics'][0]['penalty']['missed'], 
                selected_columns[32]:player['statistics'][0]['penalty']['saved'], 
            })
        )

        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit() 

            print('Dados do Jogador atualizados com sucesso')
