import asyncio
import aiohttp
from dotenv import load_dotenv
import os

load_dotenv()

async def get_ranking(url, headers, league, season):
    data = []
    resources = ['topscorers', 'topassists', 'topyellowcards', 'topredcards']

    for i in range(4):
        endpoint = f'/players/{resources[i]}?league={league}&season={season}'
        complete_url = url + endpoint
        data.append(await fetch(complete_url, headers))

    return data

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

def mount_venues_endpoint(country):
    return f'/venues?country={country}'
    # endpoint = mount_venues_endpoint() 

def mount_players_endpoint(league, season, page=1):
    return f'/players?league={league}&season={season}&page={page}'
    # endpoint = mount_players_endpoint(39, 2022)

def mount_sg_game_team_statistics_endpoint(fixture):
    return f'/fixtures/statistics?fixture={fixture}'
    # endpoint = mount_sg_game_team_statistics_endpoint(868317)

def mount_sg_game_player_statistics_endpoint(fixture):
    return f'/fixtures/players?fixture={fixture}'
    # endpoint = mount_sg_game_player_statistics_endpoint(868317)

def mount_pl_team_statistics_endpoint(league, season, team):
    return f'/teams/statistics?league={league}&season={season}&team={team}'

def mount_pl_player_statistics_endpoint(league, season):
    return f'/players?league={league}&season={season}&page=8'

async def main():
    country = 'England'
    premier_league = 39
    season = 2022
    api_key = os.getenv('API_KEY')
    url = 'https://v3.football.api-sports.io'
    headers = {
        'x-rapidapi-host': 'v3.football.api-sports.io',
        'x-rapidapi-key': api_key
    }
    endpoint = mount_pl_player_statistics_endpoint(premier_league, season)
    complete_url = url + endpoint
    data = await fetch(complete_url, headers) 
    print(data)
    # data = await get_ranking(url, headers, premier_league, season)
    # print(data[0])


asyncio.run(main())