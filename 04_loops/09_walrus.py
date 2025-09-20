# walrus operator

# There is new syntax := that assigns values to variables as part of a larger expression. It is affectionately known as “the walrus operator” due to its resemblance to the eyes and tusks of a walrus.
# ------------------------------
# value = 17
# reminder = value % 2

# if reminder: # if reminder != 0
#     print(f"Not divisible, remainder is {reminder}")

# -------------------------------
# using walrus operator
value = 17

if (reminder := value % 2): # assignment inside expression
    print(f"Not divisible, remainder is {reminder}")

# available_sizes = ["small", "medium", "large"]

# if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
#     print(f"Serving {requested_size} chai")
# else:
#     print(f"Size is unavailable - {requested_size}")

flavors = ["masala", "ginger", "lemon", "mint"]

print("Available flavors: ", flavors)

while (flavor := input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available")

print(f"You choose {flavor} chai")