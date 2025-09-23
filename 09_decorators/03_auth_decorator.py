from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied: Admins only")
            # this prevents the original function from being called
            return None
        else:
            return func(user_role)
    return wrapper

@require_admin
def acess_tea_inventory(role):
    print("Access granted to tea inventory")

acess_tea_inventory("user")
acess_tea_inventory("admin")