from datetime import datetime

from pydantic import BaseModel, field_validator, model_validator


class Person(BaseModel):
    first_name: str
    last_name: str

    @field_validator('first_name', 'last_name')
    def names_must_be_capitalize(cls, value):
        if not value.istitle():
            raise ValueError(
                "Name must contain only alphabetic characters")

        return value


class User(BaseModel):
    email: str

    @field_validator('email')
    def normalize_email(cls, value):
        return value.lower().strip()


class Product(BaseModel):
    price: str  # $4.44

    @field_validator('price', mode='before')
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v.replace('$', ''))
        return v


class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator(mode='after')
    def validate_date_range(cls, v):
        if v.start_date >= v.end_date:
            raise ValueError("Start date must be before end date")
        return v
