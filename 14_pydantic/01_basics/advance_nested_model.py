from typing import List, Optional, Union

from pydantic import BaseModel

# ----- ADVANCED PYDANTIC MODELING EXAMPLES AND NOTES -----

# Nested model pattern: Address is composed of City, which is composed of State, Country


class Country(BaseModel):
    name: str
    code: str


class State(BaseModel):
    name: str
    country: Country  # Nested model - embedding Country into State


class City(BaseModel):
    name: str
    state: State      # Nested model - embedding State into City


class Address(BaseModel):
    street: str
    city: City        # Deep nesting - Address has City, State, Country via nesting
    postal_code: str

# Demonstrates use of Optional to allow empty/missing values


class Company(BaseModel):
    name: str
    address: Optional[Address] = None  # address can be absent (null/None)

# Deeply nested model: Employee can have a Company (which itself has an Address)


class Employee(BaseModel):
    name: str
    company: Optional[Company] = None  # Nested optional

# Polymorphic/heterogeneous collection: List can contain multiple types using Union


class TextContent(BaseModel):
    type: str = "text"             # Default value pattern, handy for distinguishing types
    content: str


class ImageContent(BaseModel):
    type: str = "Image"            # Default value pattern
    # Default value for 'url' field, but can be overridden at runtime using
    url: str = 'https://example.com/image.jpg'
    alt_text: str


class Article(BaseModel):
    title: str
    sections: List[Union[TextContent, ImageContent]]
    # Advanced: sections can be a mix of text and images, using Union for runtime type distinction


article = Article(
    title="My Post",
    sections=[
        TextContent(content="Welcome to my post."),
        ImageContent(url="pic.png", alt_text="My photo"),
        TextContent(content="Goodbye!")
    ]
)

print(article.model_dump_json(indent=2))

# Organization model using nested Address models for both HQ and branches


class Organization(BaseModel):
    name: str
    head_quarter: Address
    branches: List[Address] = []   # Default: empty list for branches

# --- SUMMARY OF ADVANCED USAGE ---
# - Model composition/nesting for hierarchical/real-world data (e.g., City-State-Country)
# - Optional fields for nullable/partial API support
# - Default values for safer instantiation and clear schema docs
# - Union for lists of multiple allowed types for polymorphic/heterogeneous collections (like content blocks)
# - Deeply nested and modular model structure for clean, type-safe, and scalable schema design
# - Use of BaseModel gives you data validation, serialization, and automatic doc string generation
# - Could extend with custom validators or root_validator for complex business logic/validation rules

# Best Practice

#! Model Organization
# . 1. Define leaf models first - Models with no dependencies
# . 2. Build upward - Gradually compose more complex models (like Organization-> address->....)
# . 3. Use clear naming Make relationships obvious
# . 4. Group related models - Keep models in logical modules

#! Performance Considerations
# . 1. Deep nesting impacts performance - Keep reasonable depth
# . 2. Large lists of nested models - Consider pagination
# . 3. Circular references - Use carefully, can cause memory issues
# . 4. Lazy loading - Consider for expensive nested computations

#! Data Modeling Tips
# . 1. Model real-world relationships - Mirror your domain structure
# . 2. Use Optional appropriately - Not all relationships are required
# . 3. Consider Union types - For polymorphic relationships
# . 4. Validate bu$ness rules - Use model validators for cross-model logic
