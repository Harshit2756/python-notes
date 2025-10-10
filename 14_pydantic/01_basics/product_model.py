from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    is_available: bool = True

# correct way of using the model
product1 = Product(id=1, name="Laptop", price=999.99) 
product2 = Product(
    id=2,
    name="Smartphone",
    price=699.99,
    is_available=False
)
# here pydantic tries to convert id to the integer
product3 = Product(id="1", name="Laptop", price=999.99)

# incorrect way of using the model
product4 = Product(id=3, name="Tablet") # price is missing
product5 = Product(id="one", name="Headphones", price="invalid_price") # the id can't be converted to int

