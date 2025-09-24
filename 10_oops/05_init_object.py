# init is the constructor
class ChaiOrder:

    # we used type_ here as the type is a reserved keyword in python
    def __init__(self,size=None,type_ ="hello"):
        self.type = type_
        self.size = size
    
    def summary(self):
        return f"{self.size}ml of {self.type} chai"

# order = ChaiOrder("Masala",200)
order = ChaiOrder()
print(order.summary())

order_two = ChaiOrder("Ginger", 220)
print(order_two.summary())


