menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger chai"
]

    # [ expression for item in iterable if condition ]
iced_tea = [my_tea for my_tea in menu if "Iced" in my_tea]

print([my_tea.startswith("M") for my_tea in menu if "Tea" in my_tea])

print(iced_tea)
# Output: ['Iced Lemon Tea', 'Iced Peach Tea']