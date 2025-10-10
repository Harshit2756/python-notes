
from typing import Optional

from pydantic import BaseModel, Field


class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,  # required
        min_length=3,
        max_length=50,
        description="Employee Name",  # description for swagger
        example="Harshit"  # example like api schema for swagger
    )
    department: Optional[str] = 'General'
    salary: float = Field(
        ...,
        ge=0,  # greater than or equal to 10000
    )
    

class User(BaseModel):
    email: str = Field(..., regex=r'')
    phone: str = Field(..., regex=r'')
    age: int = Field(
        ...,
        ge=0,
        le=150,
        description="Age in years",
    )
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount percentage"
    )
