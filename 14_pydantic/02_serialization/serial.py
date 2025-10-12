from datetime import datetime
from typing import List
from pydantic import BaseModel, ConfigDict

# Serialization = converting model instances to standard formats like dict or JSON for transmission/storage.


class Address(BaseModel):
    street: str
    city: str
    zip_code: str
    # Pydantic automatically makes this class serializable (dict, JSON, etc.)


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address   # Nested model, will also be serialized recursively
    tags: List[str] = []  # List field serializes as array

    # Custom config to control JSON serialization/output
    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
        # Ensures all datetime fields are output as formatted strings in JSON, not raw Python objects
    )


# Create a User instance with nested Address field
user = User(
    id=1,
    name="Hitesh",
    email="h@hitesh.ai",
    createdAt=datetime(2024, 3, 15, 14, 30),
    address=Address(
        street="Something",
        city="Jaipur",
        zip_code="009988"
    ),
    is_active=False,
    tags=["premium", "subscriber"]
)

# ---- SERIALIZATION TO DICT ----
# Converts model (and all nested models/lists) to standard Python dict
python_dict = user.model_dump()
print(user)                      # Prints model object (helpful for debugging)
print("="*30)
# See the flat dict result; all nested Address fields are merged in
print(python_dict)

# ---- SERIALIZATION TO JSON ----
# Converts model to JSON string using encoders (e.g., for datetime)
json_str = user.model_dump_json(indent=1)
print("="*30)
# Ready to send over network, store in file, etc.
print(json_str)
