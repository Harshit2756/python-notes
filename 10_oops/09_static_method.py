class ChaiUtils:
    @staticmethod
    def make_tea():
        print("Making tea...")

    def make_coffee():
        print("Making coffee...")

    @staticmethod
    def clean_ingredients(text):
        return[item.strip().lower() for item in text.split(",")]

# Usage
ChaiUtils.make_tea()      # Output: Making tea...
raw = "water, milk, sugar, tea leaves"
ChaiUtils.make_coffee()   # Output: Making coffee...
cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)            # Output: ['water', 'milk', 'sugar', 'tea leaves']