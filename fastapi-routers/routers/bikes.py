from fastapi import APIRouter

router = APIRouter()

bikes_inventory = [
    {"id": 1, "brand": "Trek", "model": "Domane", "year": 2021, "price": 3000.0},
    {"id": 2, "brand": "Specialized", "model": "Roubaix", "year": 2020, "price": 3200.0},
    {"id": 3, "brand": "Giant", "model": "Defy", "year": 2019, "price": 2800.0},
    {"id": 4, "brand": "Cannondale", "model": "Synapse", "year": 2021, "price": 3500.0},
    {"id": 5, "brand": "Bianchi", "model": "Infinito", "year": 2020, "price": 4000.0},
]

@router.get("/all_bikes")
async def get_all_bikes():
    return {"bikes": bikes_inventory}

@router.get("/{bike_id}")
async def get_bike(bike_id: int):
    bike = next((bike for bike in bikes_inventory if bike["id"] == bike_id), None)
    if not bike:
        return {"error": "Bike not found"}
    return {"bike": bike}

@router.get("/{bikes_by_brand}")
async def get_bike_by_brand(bikes_by_brand: str):
    bike = next((bike for bike in bikes_inventory if bike["brand"] == bikes_by_brand), None)
    if not bike:
        return {"error": "Bike not found"}
    return {"bike": bike}

@router.get("/price/{min_price}/{max_price}")
async def get_bikes_by_price_range(min_price: float, max_price: float):
    filtered_bikes = [bike for bike in bikes_inventory if min_price <= bike["price"] <= max_price]
    return {"bikes": filtered_bikes}
