from typing import List, Optional

from pydantic import BaseModel, field_validator, model_validator


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address


address = Address(
    street="123 something",
    city='jaipur',
    postal_code='100011'
)

user = User(
    id=1,
    name='john',
    address=address
)

# from json to model

user_json = {
    "id": 2,
    "name": "john",
    "address": {
        "street": "123 something",
        "city": "jaipur",
        "postal_code": "100011"
    }
}

user1 = User(**user_json)

print(user)
print(user1)
