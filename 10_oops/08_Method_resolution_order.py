# Diamond Problem
class A:
    label = "A: Base class"

class B(A):
    label = "B: Derived class"

class C(A):
    label = "C: Derived class"

class D(B, C):
    pass

x = D()
# so based on the order of inheritance, B is checked first then C and then A so label of b is printed
print(x.label)
print(D.__mro__)  # Method Resolution Order

