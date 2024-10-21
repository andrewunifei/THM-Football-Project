import json

with open('players_id.json', 'w') as file:
    json.dump(players_id, file)

with open('players_id.json', 'r') as file:
    json.dump(players_id, file)