Game {
	game_id integer(4) pk unique
	referee character varying(50)
	timezone character varying(10)
	date timestamp(8)
	first_period timestamp(8)
	second_period timestamp(8)
	score json(500)
	home_team_goals integer(4)
	away_team_goals integer(4)
	venue_id integer(4) > Venue.venue_id
	home_team_id integer(4) > Team.team_id
	away_team_id integer(4) > Team.team_id
	winner_team_id integer(4) > Team.team_id
}

Venue {
	venue_id integer(4) pk unique
	name character varying(100)
	address character varying(100)
	city character varying(50)
	country character varying(50)
	capacity integer(4)
	surface character varying(25)
	image character varying(150)
}

TeamsHistoric {
	player_id integer(4) pk unique > Player.player_id
	team_id integer(4) pk unique > Team.team_id
	seasons integer(4)
}

SGTeamStatistics {
	game_id integer(4) pk unique > Game.game_id
	team_id integer(4) pk unique > Team.team_id
	shots_on_goal integer(4)
	shots_off_goal integer(4)
	total_shots integer(4)
	blocked_shots integer(4)
	shots_insidebox integer(4)
	shots_outsidebox integer(4)
	fouls integer(4)
	corner_kicks integer(4)
	offsides integer(4)
	yellow_cards integer(4)
	red_cards integer(4)
	goalkeeper_saves integer(4)
	total_passes integer(4)
	passes_accurate integer(4)
	ball_possession decimal(8)
	passes_percentage decimal(8)
	expected_goals decimal(8)
}

SGPlayerStatistics {
	player_id integer(4) pk unique > Player.player_id
	game_id integer(4) pk unique > Game.game_id
	player_number integer(4)
	position character(5)
	rating float4(4)
	captain boolean(2)
	substitute boolean(2)
	offsides integer(4)
	shots_on integer(4)
	shots_total integer(4)
	goals_total integer(4)
	goals_conceded integer(4)
	goals_assists integer(4)
	goals_saves integer(4)
	passes_total integer(4)
	passes_key integer(4)
	passes_accuracy decimal(8)
	tackles_total integer(4)
	blocks integer(4)
	interceptions integer(4)
	duels_total integer(4)
	duels_won integer(4)
	dribbles_attempts integer(4)
	dribbles_success integer(4)
	dribbles_past integer(4)
	fouls_drawn integer(4)
	fouls_committed integer(4)
	yellow_cards integer(4)
	red_cards integer(4)
	penalty_won integer(4)
	penalty_commited integer(4)
	penalty_scored integer(4)
	penalty_missed integer(4)
	penalty_saved integer(4)
}

Player {
	player_id integer pk unique
	name character varying(100)
	first_name character varying(50)
	last_name character varying(50)
	age integer(4)
	position character varying(4)
	birth json(500)
	nationality character varying(50)
	height integer(4)
	weight integer(4)
	injured boolean(2)
	photo character varying(150)
	games_apparences integer(4)
	games_lineups integer(4)
	minutes_played_total integer(4)
	rating float4(4)
	substitutes_in integer(4)
	substitutes_out integer(4)
	bench integer(4)
	shots_on integer(4)
	shots_total integer(4)
	goals_total integer(4)
	goals_conceded integer(4)
	goals_assists integer(4)
	goals_saved integer(4)
	passes_total integer(4)
	passes_key integer(4)
	passes_accuracy decimal(8)
	tackles_total integer(4)
	tackles_blocks integer(4)
	tackled_inteceptions integer(4)
	duels_total integer(4)
	duels_won_total integer(4)
	dribbles_attempts_total integer(4)
	dribbles_success_total integer(4)
	dribbles_past_total integer(4)
	fouls_drawn_total integer(4)
	fouls_committed_total integer(4)
	cards_yellow_total integer(4)
	cards_red_total integer(4)
	penalty_won_total integer(4)
	penalty_commited_total integer(4)
	penalty_scored_total integer(4)
	penalty_missed_total integer(4)
	penalty_saved_total integer(4)
	team_id integer(4) > Team.team_id
}

Injury {
	player_id integer(4) pk unique > Player.player_id
	game_id integer(4) pk unique > Game.game_id
	type character varying(50)
	reason character varying(100)
}

Team {
	team_id integer(4) pk unique
	name character varying(100)
	code character varying(25)
	country character varying(50)
	founded integer(4)
	national boolean(2)
	logo character varying(150)
	seasons_played integer(4)
	current_season integer(4)
	games_home integer(4)
	games_away integer(4)
	games_total integer(4)
	wins_home integer(4)
	wins_away integer(4)
	wins_total integer(4)
	draws_home integer(4)
	draws_away integer(4)
	draws_total integer(4)
	losses_home integer(4)
	losses_away integer(4)
	losses_total integer(4)
	goals_for_home integer(4)
	goals_for_away integer(4)
	goals_for_total integer(4)
	segments_for json(500)
	goals_against_home integer(4)
	goals_against_away integer(4)
	goal_against_total integer(4)
	segments_against json(500)
	biggest_win_home character varying(10)
	biggest_win_away character varying(10)
	biggest_loss_home character varying(10)
	biggest_loss_away character varying(10)
	clean_sheet_home integer(4)
	clean_sheet_away integer(4)
	clean_sheet_total integer(4)
	failed_to_score_home integer(4)
	failed_to_score_away integer(4)
	failed_to_score_total integer(4)
	penalty_scored integer(4)
	penalty_missed integer(4)
	yellow_cards json(500)
	red_cards json(500)
	rank integer(4)
	position integer(4)
	venue_id integer(4) > Venue.venue_id
}

