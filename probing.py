import asyncio
import aiohttp
from dotenv import load_dotenv
import os

load_dotenv()

async def fetch(url, headers):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            return await response.json()

def mount_league_endpoint(league, season):
    return f'/fixtures?league={league}&season={season}'
    # endpoint = mount_league_endpoint(39, 2022)

def mount_teams_endpoint(league, season): 
    return f'/teams?league={league}&season={season}'
    # endpoint = mount_teams_endpoint(39, 2022) 

def mount_venues_endpoint(country='England'):
    return f'/venues?country={country}'
    # endpoint = mount_venues_endpoint() 

def mount_players_endpoint(league, season, page=1):
    return f'/players?league={league}&season={season}&page={page}'
    # endpoint = mount_players_endpoint(39, 2022)

async def main():
    premier_league = 39
    season = 2022
    api_key = os.getenv('API_KEY')
    url = 'https://v3.football.api-sports.io'
    headers = {
        'x-rapidapi-host': 'v3.football.api-sports.io',
        'x-rapidapi-key': api_key
    }
    endpoint = ''
    complete_url = url + endpoint
    data = await fetch(complete_url, headers)
    print(data)

asyncio.run(main())