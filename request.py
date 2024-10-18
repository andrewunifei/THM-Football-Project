import asyncio
import aiohttp

async def fetch(url, headers):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            return await response.json()

async def main():
    headers = {
        'x-rapidapi-host': 'v3.football.api-sports.io',
        'x-rapidapi-key': 'f4604ee3d0495772e1d3e67a9d40c29a'
    }
    url = 'https://v3.football.api-sports.io'
    endpoint_league = '/fixtures?league=39&season=2022'
    complete_url = url + endpoint_league
    data = await fetch(complete_url, headers)
    print(data)

    # endpoint_fixtures = '/fixtures?league'

asyncio.run(main())