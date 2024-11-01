-- This script lists all shows of type "Comedy"
-- from the hbtn_0d_tvshows database.
-- Each record displays: tv_shows.title.
-- The results are sorted in ascending order by the title of the show

SELECT ts.title
FROM tv_shows ts
JOIN tv_show_genres tsg ON ts.id = tsg.show_id
JOIN tv_genres tg ON tsg.genre_id = tg.id
WHERE tg.name = 'Comedy'
ORDER BY ts.title ASC;
