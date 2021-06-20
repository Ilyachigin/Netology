CREATE TABLE IF NOT EXISTS Artists (id serial PRIMARY KEY, name VARCHAR (30) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS Albums (id serial PRIMARY KEY, name VARCHAR(30) NOT NULL, year INTEGER);
CREATE TABLE IF NOT EXISTS Genres (id serial PRIMARY KEY, name VARCHAR(20) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS Tracks (id serial PRIMARY KEY, name VARCHAR(20) NOT NULL, duration INTEGER NOT NULL, album_id INTEGER REFERENCES Albums(id));
CREATE TABLE IF NOT EXISTS Collection (id serial PRIMARY KEY, name VARCHAR(20) NOT NULL UNIQUE, year INTEGER);
CREATE TABLE IF NOT EXISTS ArtistsGenres (artists_id INTEGER REFERENCES Artists(id), genre_id INTEGER REFERENCES Genres(id), CONSTRAINT pk PRIMARY KEY (artists_id, genre_id));
CREATE TABLE IF NOT EXISTS AlbumArtists (artists_id INTEGER REFERENCES Artists(id), album_id INTEGER REFERENCES Albums(id), CONSTRAINT pk_artists PRIMARY KEY (artists_id, album_id));
CREATE TABLE IF NOT EXISTS CollectionTracks (collection_id INTEGER REFERENCES Collection(id), track_id INTEGER REFERENCES Tracks(id), CONSTRAINT pk_collections PRIMARY KEY (collection_id, track_id));