class Chai: 
    temperature = "hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temperature)

# attribute shadowing here if the temperature is present in the class defination
cutting.temperature = "Mild"
cutting.cup = "small"
print("After changing",cutting.temperature)
print("Direct look into the class", Chai.temperature)

# here after deleting the temperatureis will use the value defined in the class defination
del cutting.temperature
print(cutting.temperature)

# here after deleting the cup attribute it will throw error as no shadow for that or fallback for it 
cutting.cup = "small"
del cutting.cup
# print(cutting.cup)
