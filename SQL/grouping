SELECT genre_id, COUNT(artists_id) FROM artistsgenres GROUP BY genre_id;
SELECT COUNT(album_id) FROM tracks WHERE album_id IN (SELECT id FROM albums WHERE year >=2019 AND year <= 2020);
SELECT AVG(duration) FROM tracks GROUP BY album_id;
SELECT name FROM artists WHERE id IN (SELECT artists_id FROM AlbumArtists WHERE album_id IN (SELECT id FROM albums WHERE year != 2020));
SELECT name FROM collection WHERE id IN (SELECT id FROM tracks WHERE album_id IN (SELECT album_id FROM albumartists WHERE artists_id = (SELECT id FROM artists WHERE name = '5ive')));
SELECT name FROM albums WHERE id IN (SELECT album_id FROM albumartists WHERE artists_id IN (SELECT artists_id FROM artistsgenres GROUP BY artists_id HAVING COUNT (genre_id) > 1));
SELECT name FROM tracks WHERE id NOT IN (SELECT track_id FROM collectiontracks WHERE track_id IN (SELECT id FROM tracks));
SELECT name from artists WHERE id IN (SELECT artists_id FROM albumartists WHERE album_id IN (SELECT album_id FROM tracks WHERE duration = (SELECT duration FROM tracks ORDER BY duration ASC LIMIT 1)));
SELECT name FROM albums WHERE id IN (SELECT album_id FROM tracks GROUP BY album_id ORDER BY COUNT(name) ASC LIMIT 1);