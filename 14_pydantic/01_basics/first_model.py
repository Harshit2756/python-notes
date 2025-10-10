from pydantic import BaseModel

# Steps 1: import BaseModel
# Steps 2: Create a class that inherits from BaseModel
# Steps 3: Define the fields of the model using type annotations
# Steps 4: Create an instance of the model using the data you want to validate
# Steps 5: Access the validated data using the model instance always using spread/unpack operator (like ** => dict unpacking | * => list,sets,tuples unpacking )

class User(BaseModel):
    id: int # type annotations tp str
    name: str
    is_active: bool


input_data = {'id':101,'name':"Chaicode", 'is_active': True}

user = User(**input_data)
print(user)