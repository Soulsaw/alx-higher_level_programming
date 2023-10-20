-- List all genre whit the number of show linker
SELECT tv_genres.name as 'genre', COUNT(tv_show_genres.show_id) as 'number_of_shows'
FROM tv_genres
RIGHT JOIN tv_show_genres
ON tv_genres.id  = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;