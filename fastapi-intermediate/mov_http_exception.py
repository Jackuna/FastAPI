from fastapi import FastAPI,Path,Query, HTTPException

app = FastAPI()


class Movie:
    id: int
    name: str
    genre: str
    release_year: int
    imdb_rating: float

    def __init__(self, id: int, name: str, genre: str, release_year: int, imdb_rating: float):
        self.id = id
        self.name = name
        self.genre = genre
        self.release_year = release_year
        self.imdb_rating = imdb_rating

movies_inventory = [
    Movie(1, "Inception", "Sci-Fi", 2010, 8.8),
    Movie(2, "The Dark Knight", "Action", 2008, 9.0),
    Movie(3, "Interstellar", "Sci-Fi", 2014, 8.6),
    Movie(4, "Parasite", "Thriller", 2019, 8.6),
    Movie(5, "The Godfather", "Crime", 1972, 9.2),
    Movie(6, "Pulp Fiction", "Crime", 1994, 8.9),
    Movie(7, "The Shawshank Redemption", "Drama", 1994, 9.3),
    Movie(8, "Forrest Gump", "Drama", 1994, 8.8),
    Movie(9, "The Matrix", "Sci-Fi", 1999, 8.7),
    Movie(10, "Fight Club", "Drama", 1999, 8.8),
]



@app.get("/movies")
async def get_all_movies():
    return {"movies": movies_inventory}

@app.get("/movies/")
async def get_movies_by_rating(rating: float = Path(..., title="IMDB Rating", ge=0, le=10)):
    rated_movies = [movie for movie in movies_inventory if int(movie.imdb_rating) == rating]
    if not rated_movies:
        raise HTTPException(status_code=404, detail="No movies found")
    return {"movies": rated_movies}


@app.get("/movies/{movie_id}")
async def get_movie_by_id(movie_id: int = Path(..., title="The ID of the movie to get", ge=1)):
    for movie in movies_inventory:
        if movie.id == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")

@app.get("/movies/genre/{genre_name}")
async def get_movies_by_genre(rating: float = Query(..., title="IMDB Rating", ge=0, le=10), genre_name: str = Path(..., title="The genre of the movie to get")):
    genre_movies = [movie for movie in movies_inventory if movie.genre.casefold() == genre_name.casefold() and int(movie.imdb_rating) == rating]
    if not genre_movies:
        raise HTTPException(status_code=404, detail="No movies found")
    return {"movies": genre_movies}

