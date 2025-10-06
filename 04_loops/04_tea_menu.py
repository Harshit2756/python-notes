menu = ["Green", "Lemon", "Spiced", "Mint"]
# so if we want to print each item in the menu list with a counter will have to use enumerate
# enumerate(iterable, start)
help(enumerate)
for i, m in enumerate(menu, start=1): 
    print(f"Menu item {i}: {m}")