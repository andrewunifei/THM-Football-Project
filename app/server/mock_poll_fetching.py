from datetime import datetime, timedelta
import schedule
import time
import threading
import requests
from polling.game_poll import handle_polling_game
from polling.team_poll import handle_polling_team

scheduler_initialized = False

def fetch_api(league, season, db_session, api_key, engine):
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    yesterday_formated = yesterday.strftime("%Y-%m-%d")
    base_url = 'http://127.0.0.1:8080/fake/games'
    endpoint = ''
    complete_url = base_url + endpoint
    results = []

    try:
        results = handle_polling_game(complete_url, db_session, api_key)
    except Exception as e:
        print(f'Error fetching game data: {e}')

    try: 
        if len(results) > 0:
            for result in results:
                handle_polling_team(engine, db_session, 0)
                handle_polling_team(engine, db_session, 1)
        else:
            return False
    except Exception as e:
        print(f'Error fetching team data: {e}')

def run_schedule(league, season, db_session, api_key, engine):
    global scheduler_initialized

    if not scheduler_initialized:
        schedule.every().day.at("21:26").do(lambda: fetch_api(league, season, db_session, api_key, engine))
        scheduler_initialized = True

    while True:
        schedule.run_pending()
        time.sleep(60)
