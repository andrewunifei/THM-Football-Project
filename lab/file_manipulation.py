"""
Laboratório

Usar essa lógica para armazenar IDs de jogadores em um arquivo de texto
"""
import json

players_id = [1,2,3,4,5,6,7,8,9]
data_list = []

with open('players_id.json', 'w') as file:
    json.dump(players_id, file)

with open('players_id.json', 'r') as file:
    data_list = json.load(file)

print(data_list) # Funcionando