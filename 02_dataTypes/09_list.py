# List operations and methods
ingredients = ["water", "milk", "black tea"]

#  access at aparticular index
print(f"First ingredient: {ingredients[0]}")
print(f"Last ingredient: {ingredients[-1]}")

# append: adds an element to the end of the list
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")
# remove: removes the first occurrence of a value
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

# extend: adds all elements of an iterable (like another list) to the end
chai_ingredients.extend(spice_options)
print(f"chai extends: {chai_ingredients}")

# insert: adds an element at a specific position
chai_ingredients.insert(2, "black tea")
print(f"chai inset at 2: {chai_ingredients}")

# remove: removes the first occurrence of a value
last_added = chai_ingredients.pop()
print(f"{last_added}")
print(f"chai pop: {chai_ingredients}")
# reverse: reverses the list in place
chai_ingredients.reverse()
print(f"chai reverse: {chai_ingredients}")
# sort: sorts the list in place
chai_ingredients.sort()
print(f"chai sort: {chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix: {full_liquid_mix}")

strong_brew = ["black tea", "water"] * 3
print(f"String brew: {strong_brew}")

# split 
veggies = "tomato cucumber spinach"
# Convert string to list
veggie_list = veggies.split()

print(veggie_list)

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")