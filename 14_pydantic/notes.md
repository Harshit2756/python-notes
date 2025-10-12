### Pydantic

Pydantic is a data validation and parsing library for Python. It uses Python type hints to automatically check, convert, and serialize data — without you writing manual validation code.

#### How it’s used in real projects:

- ✅ Data parsing and validation
- ✅ API Input Validation (e.g. FastAPI request bodies)
- ✅ Data Serialization (convert to/from dict or JSON)
- ✅ Configuration Models (load .env or JSON configs safely)

#### ⚙️ Pydantic Flow — Step-by-Step (Clean & Clear)

[first_model.py](./01_basics/first_model.py)
🧩 **Step 1: Import BaseModel**

```python
from pydantic import BaseModel
```

`BaseModel` is the core class in Pydantic. It gives your model automatic validation, type conversion, and serialization.

🧩 **Step 2: Create a Class that Inherits from BaseModel**

```python
class User(BaseModel):
    ...
```

You define your schema (structure) by subclassing `BaseModel`. Each subclass becomes a data model with its own validation rules.

🧩 **Step 3: Define Fields with Type Hints**

```python
class User(BaseModel):
    id: int
    name: str
    is_active: bool = True  # optional with default
```

These type annotations (`int`, `str`, etc.) tell Pydantic how to validate input. Default values make a field optional.

🧩 **Step 4: Create an Instance (Validation Happens Here)**

```python
user = User(id="42", name="Harshit")
```

When you create an instance, Pydantic:

- Checks if each field exists.
- Validates and converts the data.
- Raises a `ValidationError` if anything’s wrong.

✅ **Works**:

```python
User(id="42", name="Harshit")  # auto-converts id → int
```

❌ **Fails**:

```python
User(id="abc", name="Harshit")  # cannot convert string to int
```

🧩 **Step 5: Access Validated Data**

```python
print(user.id)        # 42
print(user.name)      # Harshit
print(user.model_dump())    # {'id': 42, 'name': 'Harshit', 'is_active': True}
```

- `.model_dump()` returns a Python dict of validated data.
- `.model_dump_json()` gives you a JSON string version.

#### ⚙️ About the Unpacking Operator (\*_ / _)

Yes 💯 — you can use them to unpack data into a model:

```python
data = {"id": 1, "name": "Harshit"}
user = User(**data)  # Unpacks dict into keyword args
```

Or the other way around:

```python
print(**user.model_dump())  # Unpacks model back into arguments
```

🧠 Think of ** as "spread this dictionary’s keys and values into parameters." That’s super common when you pass Pydantic models into functions or APIs.

### Lesson 2: Type Conversion & Field Validation (Pydantic 101 advanced)

🧩 **1️⃣ Type Conversion (a.k.a. Smart Parsing)**
Pydantic auto-converts compatible types. Check this out 👇
[product_model.py](./01_basics/product_model.py)

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    is_active: bool

user = User(name="Harshit", age="23", is_active="true")
print(user)
```

🧠 **What happens**:

- "23" → converted to int(23)
- "true" → converted to bool(True)

✅ **Output**:

```python
name='Harshit' age=23 is_active=True
```

So yeah — no manual conversions. Pydantic auto-parses your input into proper Python types.

🧩 **2️⃣ Field Validation**
Now, we can define rules (constraints) for each field. We use `Field()` for this 👇
[field_example.py](./01_basics/field_example.py)

| Constraint | What It Does | How to Use |
|------------|--------------|-------------|
| `min_length` | Minimum length for strings | `name: str = Field(..., min_length=3)` |
| `max_length` | Maximum length for strings | `name: str = Field(..., max_length=50)` |
| `ge` | Greater than or equal (for numbers) | `age: int = Field(..., ge=18)` |
| `gt` | Greater than (strictly) | `price: float = Field(..., gt=0)` |
| `le` | Less than or equal (for numbers) | `age: int = Field(..., le=60)` |
| `lt` | Less than (strictly) | `score: int = Field(..., lt=100)` |
| `regex` | Pattern match for strings | `email: str = Field(..., regex=r'^\S+@\S+\.\S+$')` |

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., ge=18, le=100)
    email: str = Field(..., pattern=r'^\S+@\S+\.\S+$')
```

🧠 **Meaning**:

- `min_length`, `max_length` → string size limits
- `ge` (greater or equal), `le` (less or equal) → numeric limits
- `pattern` → regex pattern validation

**Example**:

```python
user = User(name="Harshit", age=22, email="harshit@gmail.com")
print(user)
```

✅ **Works fine**.

But if you pass:

```python
User(name="Ha", age=15, email="invalidemail")
```

❌ **Raises ValidationError**:

```python
pydantic.error_wrappers.ValidationError: 3 validation errors for User
```

🧩 **3️⃣ Default Values + Optional Fields**
If a field isn’t mandatory — use `Optional`.
[optional_example.py](./01_basics/optional_example.py)

```python
from typing import Optional

class User(BaseModel):
    name: str
    age: int
    # Optional[dataType] =  Defalut value
    phone: Optional[str] = None  # optional field with default None
```

🧩 **4️⃣ Example: Combined Model**

```python
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class User(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., ge=18, le=60)
    email: EmailStr
    phone: Optional[str] = Field(None, pattern=r'^\d{10}$')  # 10-digit number
```

✅ **Valid input**:

```python
user = User(name="Harshit", age=23, email="harshit@gmail.com", phone="9876543210")
print(user)
```

❌ **Invalid phone or email → instant validation error**.

🧩 **5️⃣ Field Aliases (bonus tip)**
If you receive JSON keys with different names:

```python
class User(BaseModel):
    full_name: str = Field(..., alias="fullName")
```

Now:

```python
data = {"fullName": "Harshit Khandelwal"}
user = User(**data)
print(user.full_name)  # ✅ works
```

💡 **In short Pydantic automatically**:

- Converts data types
- Validates constraints
- Raises errors for invalid data
- Keeps your data clean AF 😎
