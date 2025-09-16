# for else

people = [("John",10), ("Jane", 17), ("Doe", 13), ("Alice", 12)]

for name, age in people:
    if age >= 18:
        print(name, "is an adult.")
        break
else:
    print("All people are minors.")
