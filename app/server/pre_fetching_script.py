import os
from controller.pre_fetching.venue_fetching import fetch_venue
from dotenv import load_dotenv

load_dotenv()
postgres_user = os.getenv('POSTGRES_USER')
postgres_passwd = os.getenv('POSTGRES_PASSWD')
api_key = os.getenv('API_KEY')

fetch_venue(postgres_user, postgres_passwd, api_key)