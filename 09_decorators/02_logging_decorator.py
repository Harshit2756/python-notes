from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🚀 Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✅ Finished: {func.__name__}")
        return result
    return wrapper

def boil_milk(liters):
    @wraps(liters)
    def inner():
        print(f"Boiling {liters} liters of milk")
    return inner

@log_activity
def brew_chai(type):
    print(f"Brewing {type} chai and milk status ")

brew_chai("Masala")

# can we use multiple decorators on a single function?
