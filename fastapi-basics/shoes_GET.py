from fastapi import Body, FastAPI

app = FastAPI()

shoes_inventory = [
    {"id": 1, "name": "Nike Air Max", "type": "Sneakers", "price": 120.0, "brand": "Nike"},
    {"id": 2, "name": "Adidas Ultraboost", "type": "Running", "price": 180.0, "brand": "Adidas"},
    {"id": 3, "name": "Puma Suede Classic", "type": "Casual", "price": 80.0, "brand": "Puma"},
    {"id": 4, "name": "Reebok Club C 85", "type": "Casual", "price": 70.0, "brand": "Reebok"},
    {"id": 5, "name": "New Balance 990v5", "type": "Running", "price": 175.0, "brand": "New Balance"},
    {"id": 6, "name": "Asics Gel-Kayano 27", "type": "Running", "price": 160.0, "brand": "Asics"},
    {"id": 7, "name": "Converse Chuck Taylor", "type": "Casual", "price": 55.0, "brand": "Converse"},
    {"id": 8, "name": "Vans Old Skool", "type": "Casual", "price": 60.0, "brand": "Vans"},
    {"id": 9, "name": "Under Armour HOVR Phantom", "type": "Running", "price": 140.0, "brand": "Under Armour"},
    {"id": 10, "name": "Brooks Ghost 13", "type": "Running", "price": 130.0, "brand": "Brooks"},

]

# Path parameter example for a Basic route that returns a welcome message
@app.get("/")
async def firstAPI():
    return {"message": "Hello From FastAPI"}

# Path parameter example endpoint to get all shoes
@app.get("/shoes")
async def get_all_shoes():
    return {"shoes": shoes_inventory}

# Path parameter example to get information about the shoes API and an example of order of routes
# FastAPI matches routes in the order they are defined, so more specific routes should be defined before more general ones.

@app.get("/shoes/about")
async def get_shoes_about():
    return {"about": "This is a simple API for managing a shoe inventory."}

# Path Parameters with Dynamic Values example
# this endpoint can be called like /shoes/Nike

@app.get("/shoes/{shoe_brand}")
async def get_shoes_by_brand(shoe_brand):
    for shoe in shoes_inventory:
        if shoe.get("brand").lower() == shoe_brand.lower():
            return shoe

    return {"message": "Shoe not found"}

# Query Parameters example
# this endpoint can be called like /shoes/?shoe_type=Running

@app.get("/shoes/")
async def get_shoes_by_type(shoe_type: str):

    # shoes_by_type = []
    # for shoe in shoes_inventory:
    #     if shoe.get("type").casefold() == shoe_type.casefold():
    #         shoes_by_type.append(shoe)
    #     else:
    #         pass

    # List comprehension to filter shoes by type
    shoes_by_type = [shoe for shoe in shoes_inventory if shoe.get("type").casefold() == shoe_type.casefold()]
    return shoes_by_type

# Combination of Path and Query Parameters example
# Using this we can search for a shoe by brand and filter by type
# this endpoint can be called like /shoes/Nike/?shoe_type=Running

@app.get("/shoes/{shoe_type}/")
async def get_shoes_by_brand_and_type(shoe_type: str, shoe_brand: str):
    get_shoes_by_brand_and_type = [ shoe for shoe in shoes_inventory if shoe.get("type").casefold() == shoe_type \
                                   and shoe.get("brand").casefold() == shoe_brand]
    
    return get_shoes_by_brand_and_type
