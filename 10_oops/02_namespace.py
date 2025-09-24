class Chai:
    origin = "India"

print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)


# creating objects from class chai
 
masala = Chai()
print(f"Masala {masala.origin}")
print(f"Masala  {masala.is_hot}")

masala.is_hot = False
masala.flavour = False

# print("Class: ", Chai.flavour)
print("Masala: ", masala.flavour)
