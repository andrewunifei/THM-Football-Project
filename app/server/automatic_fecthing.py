from datetime import datetime, timedelta
import schedule
import time
import threading
import requests

def fetch_api(league, season):
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    yesterday_formated = yesterday.strftime("%Y-%m-%d")
    api_endpoint = f'/fixtures?league={league}&season={season}&date={yesterday_formated}'

    try:
        response = requests.get('https://api.example.com/data')  # Replace with your API URL
        if response.status_code == 200:
            print('Data fetched:', response.json())
        else:
            print('Failed to fetch data:', response.status_code)
    except Exception as e:
        print(f'Error fetching data: {e}')

def run_schedule():
    schedule.every().day.at("05:00").do(fetch_api)

    while True:
        schedule.run_pending()
        time.sleep(60)