from pydantic import BaseModel, Field, computed_field


class Product(BaseModel):
    price: float
    quantity: int

    # Now computed field decorator marks the field as computed.That means it will be calculated on the go.
    @computed_field
    @property  # This is a property decorator. It is used to define a property in a class so that it's accessible as a parameter
    def total_price(self) -> float:
        return self.price * self.quantity


class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_night: float

    @computed_field
    @property
    def total_price(self) -> float:
        return self.nights * self.rate_per_night


booking = Booking(user_id=1, room_id=101, nights=3, rate_per_night=100.)

print(booking.total_price)
print(booking.model_dump()) # total price will be there in the 


