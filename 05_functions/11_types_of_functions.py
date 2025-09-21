# Pure functions
def pure_chai(cups):
    return cups * 10

total_chai = 0

# Impure Function - not recommended
def impure_chai(cups):
    global total_chai
    total_chai += cups

# Recursive functions
def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups poured"
    return pour_chai(n-1)

print(pour_chai(3))

chai_types = ["light", "kadak", "ginger", "kadak"]

# anonymous functions (lambda)
# filter (function, iterable) so here function is lambda chai: chai!="kadak" which fill return True or False for each chai in chai_types list and if the result is True then that chai will be added to the new list strong_chai
strong_chai = list(filter(lambda chai: chai!="kadak", chai_types))
# without lambda
def is_strong(chai):
    return chai != "kadak"

a_chai = list(filter(is_strong, chai_types))

print(a_chai)
print(strong_chai)