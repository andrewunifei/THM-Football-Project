select distinct team.name, team.logo FROM team
inner join player on player.team_id = team.team_id
order by team.name

SELECT injury.* FROM injury
join player on injury.player_id = player.player_id
where player.player_id = 

SELECT DISTINCT reason FROM injury

SELECT * FROM teamshistoric
ORDER BY player_id ASC, team_id ASC 