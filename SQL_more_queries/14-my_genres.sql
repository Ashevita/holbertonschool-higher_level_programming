-- This script lists all genres of the show "Dexter"
-- from the hbtn_0d_tvshows database.
-- Each record displays: tv_genres.name.
-- The results are sorted in ascending order by genre name.

SELECT tg.name
FROM tv_genres tg
JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
JOIN tv_shows ts ON tsg.show_id = ts.id
WHERE ts.title = 'Dexter'
ORDER BY tg.name ASC;
