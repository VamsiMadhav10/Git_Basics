from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


products = [
    {"id": 1, "name": "Laptop", "price": 75000, "category": "Electronics"},
    {"id": 2, "name": "Smartphone", "price": 25000, "category": "Electronics"},
    {"id": 3, "name": "Shoes", "price": 8000, "category": "Footwear"},
    {"id": 4, "name": "Backpack", "price": 1200, "category": "Accessories"},
]

class Product(BaseModel):
    name: str
    price: float
    category: str



@app.get("/products")
def get_products():
    return products


@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/products", status_code=201)
def add_product(product: Product):
    new_id = max(p["id"] for p in products) + 1 if products else 1
    new_product = product.dict()
    new_product["id"] = new_id
    products.append(new_product)
    return new_product
