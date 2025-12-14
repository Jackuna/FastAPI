from fastapi import FastAPI
from routers import cars, auth, bikes

app = FastAPI()

app.include_router(cars.router)
app.include_router(auth.router)
app.include_router(bikes.router, prefix="/bikes", tags=["bikes"])

