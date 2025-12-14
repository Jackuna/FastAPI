from fastapi import APIRouter

router = APIRouter()


cars_inventory = [
    {"id": 1, "make": "Toyota", "model": "Camry", "year": 2020, "price": 24000.0},
    {"id": 2, "make": "Honda", "model": "Civic", "year": 2019, "price": 22000.0},
    {"id": 3, "make": "Ford", "model": "Mustang", "year": 2021, "price": 26000.0},
    {"id": 4, "make": "Chevrolet", "model": "Malibu", "year": 2018, "price": 21000.0},
    {"id": 5, "make": "Nissan", "model": "Altima", "year": 2020, "price": 23000.0},
    {"id": 6, "make": "BMW", "model": "3 Series", "year": 2021, "price": 41000.0},
    {"id": 7, "make": "Audi", "model": "A4", "year": 2019, "price": 39000.0},
    {"id": 8, "make": "Mercedes-Benz", "model": "C-Class", "year": 2020, "price": 42000.0},
    {"id": 9, "make": "Volkswagen", "model": "Passat", "year": 2018, "price": 20000.0},
    {"id": 10, "make": "Hyundai", "model": "Sonata", "year": 2021, "price": 25000.0} ]

# Path parameter example for a Basic route that returns a welcome message
@router.get("/")
async def firstAPI():
    return {"message": "Hello From Cars API"}

# Path parameter example endpoint to get all cars
@router.get("/cars")
async def get_all_cars():
    return {"cars": cars_inventory}

