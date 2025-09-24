# features  |  class methods  |  static methods
# ------------------------------------------------
# first parameter  |  cls            |  none
# Use Case         |  Operate on the class , not instance |  Utility functions related to the class
# Access to cls  |  Yes            |  No
# Access to self |  No             |  No

class ChaiOrder:
    def __init__(self , tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )
    
    @classmethod
    def from_string(cls, order_str):
        tea_type, sweetness, size = order_str.split("-")
        return cls(tea_type, sweetness, size)
    
# Usage
order1 = ChaiOrder.from_dict({
    "tea_type": "Masala",
    "sweetness": "Medium",
    "size": "Large"
})

order2 = ChaiOrder.from_string("Ginger-Low-Small")

print(order1.__dict__)  # Output: {'tea_type': 'Masala', 'sweetness': 'Medium', 'size': 'Large'}
print(order2)  # Output: {'tea_type': 'Masala', 'sweetness': 'Medium', 'size': 'Large'}
print(order2.__dict__)  # Output: {'tea_type': 'Ginger', 'sweetness': 'Low', 'size': 'Small'}