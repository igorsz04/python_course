get_rider_id_query = """
select id_r from riders where riderlastname='%s';
"""

get_riders_id_query = """
select id_r from riders;
"""

get_riders_all_query = """
select * from rider_average_skills; 
"""

get_rounds_all_query = """
select * from series_calendar;
"""

get_teams_all_query = """
select * from teams;
"""


get_track_id_query = """
SELECT id_t FROM tracks where track = '%s';
"""



# add row with title, rel_year, durarion, rating, voters, ranking,
#         orig_title

add_film_row_query = """
INSERT INTO film (title, relYear, durationMins, rating, voters, ranking, directorID) VALUES
('%s', %s, %s, %s, %s, %s, %s);
"""

add_actor_in_film_row = """
INSERT INTO actor_in_film (filmID, actorID) VALUES (%s, %s);
"""

add_film_has_genre_row = """
INSERT INTO film_has_genre (filmID, genreID) VALUES (%s, %s);
"""