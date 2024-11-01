from datetime import datetime, timedelta
import schedule
import time
import threading
import requests
from polling.game_poll import handle_polling_game
from polling.team_poll import handle_polling_team

def fetch_api(league, season, db_session, api_key):
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    yesterday_formated = yesterday.strftime("%Y-%m-%d")
    base_url = 'https://api.example.com/'
    endpoint = f'fixtures?league={league}&season={season}&date={yesterday_formated}'
    complete_url = base_url + endpoint

    try:
        results = handle_polling_game(complete_url, db_Session, api_key)
        if len(results) > 0:
            for result in results:
                handle_polling_team(db_session, result[0])
                handle_polling_team(db_session, result[1])
            print(results)
        else:
            False

    except Exception as e:
        print(f'Error fetching data: {e}')

def run_schedule():
    schedule.every().day.at("05:00").do(fetch_api)

    while True:
        schedule.run_pending()
        time.sleep(60)
