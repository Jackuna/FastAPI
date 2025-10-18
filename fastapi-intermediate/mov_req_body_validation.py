from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Movie:
    id: int
    name: str
    genre: str
    release_year: int
    imdb_rating: float

    def __init__(self, id, name, genre, release_year, imdb_rating):
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


class MovieRequestData(BaseModel):
    id: int
    name: str
    genre: str
    release_year: int
    imdb_rating: float

@app.get("/movies")
async def get_all_movies():
    return {"movies": movies_inventory}

@app.post("/movies/add_movie")
async def add_movie_data(new_movie_req: MovieRequestData):
    movie_data = Movie(**new_movie_req.model_dump())
    movies_inventory.append(movie_data)
    return movies_inventory

