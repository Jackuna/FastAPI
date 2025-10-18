from fastapi import FastAPI, Body

app = FastAPI()

shoes_inventory = [
    {"id": 1, "name": "Nike Air Zoom Pegasus 37", "type": "Running", "price": 120.0, "brand": "Nike"},
    {"id": 2, "name": "Adidas Ultraboost 21", "type": "Running", "price": 180.0, "brand": "Adidas"},
    {"id": 3, "name": "Puma RS-X3", "type": "Casual", "price": 110.0, "brand": "Puma"},
    {"id": 4, "name": "Reebok Nano X1", "type": "Training", "price": 130.0, "brand": "Reebok"},
    {"id": 5, "name": "New Balance Fresh Foam 1080v11", "type": "Running", "price": 150.0, "brand": "New Balance"},
    #{"id": 6, "name": "Asics Gel-Nimbus 23", "type": "Running", "price": 160.0, "brand": "Asics"},
    #{"id": 7, "name": "Converse Chuck 70", "type": "Casual", "price": 85.0, "brand": "Converse"},
    #{"id": 8, "name": "Vans Sk8-Hi", "type": "Casual", "price": 75.0, "brand": "Vans"},
    #{"id": 9, "name": "Under Armour Curry 8", "type": "Basketball", "price": 140.0, "brand": "Under Armour"},
    #{"id": 10, "name": "Brooks Adrenaline GTS 21", "type": "Running", "price": 130.0, "brand": "Brooks"},
]

# POST endpoint to add a new shoe to the inventory
# Path parameter example endpoint to get all shoes
@app.get("/shoes")
async def get_all_shoes():
    return {"shoes": shoes_inventory}

# POST endpoint to add a new shoe to the inventory
@app.post("/shoes/add_shoe")
async def add_new_shoe(shoe_details=Body()):
    shoes_inventory.append(shoe_details)
