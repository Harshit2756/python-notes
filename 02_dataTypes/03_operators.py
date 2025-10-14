# Integer

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is {total_grams}")

remaining_tea = black_tea_grams - ginger_grams
print(f"Total grams of remaining tea is {remaining_tea}")

#  Exact division 
milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving is {milk_per_serving}")

# Floor division (to the lower whole number)
total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"Whole tea bags per pot: {bags_per_pot}")

# Modulus (Remainder)
total_cardamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cardamom_pods % pods_per_cup
print(f"Leftover Cardamom pods: {leftover_pods}")

# Exponentiation
base_flavor_strength = 2
scale_factor = 3
powerful_flavor = base_flavor_strength ** scale_factor
print(f"Scaled flavour strength {powerful_flavor}")
# 2 * 2 * 2

total_tea_leaves_harvested = 1_000_000_000
print(f"tea leaves: {total_tea_leaves_harvested}")

# operator overloading