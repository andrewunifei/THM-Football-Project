--
SELECT game.timezone, game.date FROM game
join injury on injury.game_id = game.game_id

--
SELECT DISTINCT EXTRACT(YEAR FROM game.date) AS year
FROM game
ORDER BY year;

--
SELECT *
FROM game
WHERE EXTRACT(YEAR FROM date) = inputed_year;