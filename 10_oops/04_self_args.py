class Chaicup:
    # methods ar functions inside the class 
    size = 150 

    # self is the reference to all the properties and method defined in this class
    def describe(self):
        return f"A {self.size}ml chai cup"
        
cup = Chaicup()
print(cup.describe())
# here error as it requires self and python don't known which context(object values) to use. 
# print(Chaicup.describe())
print(Chaicup.describe(cup))

cup_two = Chaicup()
cup_two.size=100
print(cup_two.describe())
print(Chaicup.describe(cup_two))
