
chai_type = "ginger"
def update_order():
    def kitchen():
        nonlocal chai_type # Referencing the nearest enclosing scope variable
        print("In kitchen before update", chai_type)
        chai_type = "Kesar"
    chai_type = "Elaichi"
    kitchen()
    print("After kitchen update", chai_type)

update_order()
print("In global scope", chai_type)