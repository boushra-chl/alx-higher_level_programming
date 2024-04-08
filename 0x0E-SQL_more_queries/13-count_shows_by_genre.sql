--  lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_show_genres.name AS genre, COUNT(tv_shows.id) AS number_of_shows
FROM tv_show_genres
JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
GROUP BY tv_show_genres.genre
ORDER BY number_of_shows DESC;
