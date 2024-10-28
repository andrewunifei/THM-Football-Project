SELECT game.timezone, game.date FROM game
join injury on injury.game_id = game.game_id