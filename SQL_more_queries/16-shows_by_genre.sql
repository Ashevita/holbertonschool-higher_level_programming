-- This script lists all shows and genres related to each show
-- from the hbtn_0d_tvshows database.
-- Each record displays: tv_shows.title - tv_genres.name.
-- If a show has no genre, NULL will be displayed in the genre column.
-- The results are sorted in ascending order by show title and genre name.

SELECT ts.title, tg.name
FROM tv_shows ts
LEFT JOIN tv_show_genres tsg ON ts.id = tsg.show_id
LEFT JOIN tv_genres tg ON tsg.genre_id = tg.id
ORDER BY ts.title ASC, tg.name ASC;
