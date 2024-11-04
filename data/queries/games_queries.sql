--
SELECT game.timezone, game.date FROM game
join injury on injury.game_id = game.game_id

--
SELECT DISTINCT EXTRACT(YEAR FROM game.date) AS year
FROM game
ORDER BY year;

--
SELECT 
	game.*,
    home_team.name AS home_team,
    away_team.name AS away_team
FROM 
    game
JOIN 
    team AS home_team ON game.home_team_id = home_team.team_id
JOIN 
    team AS away_team ON game.away_team_id = away_team.team_id
WHERE EXTRACT(YEAR FROM date) =  AND EXTRACT(MONTH FROM date) = 

--
SELECT
	game.*,
	venue.*,
	home_team.name AS home_team,
	home_team.code AS home_code,
	home_team.logo AS home_logo,
    away_team.name AS away_team,
	away_team.code AS away_code,
	away_team.logo AS away_logo
FROM game
JOIN 
    team AS home_team ON game.home_team_id = home_team.team_id
JOIN 
    team AS away_team ON game.away_team_id = away_team.team_id
JOIN
	venue on game.venue_id = venue.venue_id
WHERE game.game_id = 

--
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'game';