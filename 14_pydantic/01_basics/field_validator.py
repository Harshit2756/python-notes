from pydantic import BaseModel, field_validator, model_validator


class User(BaseModel):
    username: str

    @field_validator('username')
    def username_length(cls, v):
        # Check if the username length is at least 3 characters
        if len(v) < 3:
            raise ValueError("Username must be at least 3 characters long")
        # Return the validated value so Pydantic can assign it to the field
        return v  # It's necessary to return the value so the model receives the validated data


# Define a data model for user signup, requiring password confirmation


class SignupData(BaseModel):
    password: str
    confirm_password: str

    # Field validator: Validates and processes an INDIVIDUAL field (password)
    @field_validator('password')
    def password_strength(cls, v):
        # Ensure password is at least 8 characters long
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        # (Optional) You can also add checks for digits, uppercase, etc. here
        return v  # The checked (or transformed) value MUST be returned!

    # Model validator: Validates RELATIONSHIP between MULTIPLE fields.
    # mode after=> means after field validators are run then this will run
    @model_validator(mode="after")
    def passwords_match(self):
        # self is the instance; access fields as self.password, self.confirm_password
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        # Return self for Pydantic to complete model creation
        return self

# ----------------------------
# How this works in practice:
# ----------------------------

# 1. When you create a new SignupData object, Pydantic will:
#    A. Run the password field validator to check its length.
#    B. Run the model validator to confirm both password fields match.
#    C. Raise errors if any checks fail; otherwise, return the validated object.


# ----------------------------
# Example usage:
# ----------------------------
try:
    user = SignupData(password="strongpass", confirm_password="strongpass")
    print("Signup successful:", user)
except Exception as e:
    print("Signup failed:", e)

try:
    user = SignupData(password="short", confirm_password="short")
except Exception as e:
    print("Signup failed:", e)  # Fails password length check

try:
    user = SignupData(password="strongpass", confirm_password="wrongpass")
except Exception as e:
    print("Signup failed:", e)  # Fails passwords match check
