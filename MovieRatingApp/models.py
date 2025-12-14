from database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean

class RateMovie(Base):
    __tablename__ = "movieratings"

    id = Column(Integer, primary_key=True, index=True)
    movie_name = Column(String, index=True)
    rating = Column(Float)
    release_year = Column(Integer)
    genre = Column(String)
    must_watch = Column(Boolean)
