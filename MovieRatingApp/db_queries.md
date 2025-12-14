# Queries used in the project for database operations

CREATE TABLE movieratings (
    id = INTEGER NOT NULL,
    movie_name VARCHAR,
    rating FLOAT,
    release_year INTEGER,
    genre VARCHAR,
    PRIMARY KEY (id)
);

# Insert data into movieratings TABLE

insert into movieratings (movie_name, rating, release_year, genre, must_watch) values ('Inception', 8.8, 2010, 'Sci-Fi', True)
Update below lines with above context data format

insert into movieratings (movie_name, rating, release_year, genre, must_watch) values ('Inception', 8.8, 2010, 'Sci-Fi', True)
insert into movieratings (movie_name, rating, release_year, genre, must_watch) values ('The Dark Knight', 9.0, 2008, 'Action', True)
insert into movieratings (movie_name, rating, release_year, genre, must_watch) values ('Interstellar', 8.6, 2014, 'Sci-Fi', True)
insert into movieratings (movie_name, rating, release_year, genre, must_watch) values ('Parasite', 8.6, 2019, 'Thriller', True)
insert into movieratings (movie_name, rating, release_year, genre, must_watch) values ('The Godfather', 9.2, 1972, 'Crime', True)
insert into movieratings (movie_name, rating, release_year, genre, must_watch) values ('Pulp Fiction', 8.9, 1994, 'Crime', True)
insert into movieratings (movie_name, rating, release_year, genre, must_watch) values ('The Shawshank Redemption', 9.3, 1994, 'Drama', True)
insert into movieratings (movie_name, rating, release_year, genre, must_watch) values ('Forrest Gump', 8.8, 1994, 'Drama', True)
insert into movieratings (movie_name, rating, release_year, genre, must_watch) values ('The Matrix', 8.7, 1999, 'Sci-Fi', True);
insert into movieratings (movie_name, rating, release_year, genre, must_watch) values ('Fight Club', 8.8, 1999, 'Drama', True);
