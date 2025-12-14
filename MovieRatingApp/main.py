from fastapi import Depends, FastAPI
import models
from database import SessionLocal, engine
from typing import Annotated
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
        
@app.get("/")
async def root():
    return {"message": "Welcome to the Movie Rating App!"}

@app.get("/movies")
async def read_all_movies(db: db_dependency):
    movies = db.query(models.RateMovie).all()
    return movies

