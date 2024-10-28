-- Informações básicas dos times
select name, code, country, founded, logo from team
where games_played_total > 0

-- Estatísticas sobre jogos de um time
select
	games_played_home,
	games_played_away,
	games_played_total,
	wins_home,
	wins_away,
	wins_total,
	losses_home,
	losses_away,
	losses_total,
	draws_home,
	draws_away,
	draws_total,
from team
where games_played_total > 0 and code = code

-- Estatísticas sobre gols de um time
select
	goals_for_home,
	goals_for_away,
	goals_for_total,
	segments_for,
	goals_against_home,
	goals_against_away,
	goals_against_total,
	segments_against
from team
where games_played_total > 0 and code = 'MUN'