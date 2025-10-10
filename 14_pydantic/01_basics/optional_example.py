from typing import Dict, List, Optional
from pydantic import BaseModel


class Cart(BaseModel):
    user_id: int
    items: List[Dict[str, int]] 

class BlogPost(BaseModel):
    title: str
    content: str
    imafe_url: Optional[str] = None # optional field with default value(None)


cart_data = {
    "user_id": 123,
    "items": [
        {"product_id": 1, "quantity": 2},
        { "product_id": 2, "quantity": 1 },
    ],
    "extra_field": "this will be ignored"
}

cart = Cart(**cart_data) # or cart_data.unpack()
print(cart)
print(cart.model_dump()) # convert to dict
print(cart.model_dump_json())# 