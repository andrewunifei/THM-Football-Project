from datetime import datetime, timedelta
import schedule
import time
import threading
import requests
from polling.game_poll import handle_polling_game
from polling.team_poll import handle_polling_team
from polling.player_poll import handle_polling_player
from polling.injury_poll import handle_polling_injury

scheduler_initialized = False

def fetch_api(league, season, db_session, api_key, engine):
    # Regra de negócio: automaticamente busca por dados de jogos do dia anterior
    # Todo dia as 5 horas da manhã
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    yesterday_formated = yesterday.strftime("%Y-%m-%d")
    base_url = f'https://v3.football.api-sports.io/{injuries_endpoint}'
    endpoint = f'fixtures?league={league}&season={season}&date={yesterday_formated}'
    complete_url = base_url + endpoint
    results = []

    try:
        results = handle_polling_game(complete_url, db_session, api_key)
    except Exception as e:
        print(f'Erro ao buscar dados sobre novos jogos: {e}')

    try: 
        if len(results) > 0:
            for result in results:
                handle_polling_team(engine, db_session, result[0])
                handle_polling_team(engine, db_session, result[1])
                handle_polling_player(engine, db_session, api_key, league, season, result[0])
                handle_polling_player(engine, db_session, api_key, league, season, result[1])
                handle_polling_injury(api_key, league, season, result[2], db_session)
        else:
            return False
    except Exception as e:
        print(f'Erro ao atualizar dados sobre times: {e}')

def run_schedule(league, season, db_session, api_key, engine):
    global scheduler_initialized

    if not scheduler_initialized:
        schedule.every().day.at("05:00").do(lambda: fetch_api(league, season, db_session, api_key, engine))
        scheduler_initialized = True

    while True:
        schedule.run_pending()
        time.sleep(60)
