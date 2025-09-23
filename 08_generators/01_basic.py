# save memory by yielding items one by one
# don't want to store all items in memory at once
# lazy evaluation

def serve_chai():
    yield "Step 1: Boil water"
    yield "Step 2: Add tea leaves"
    yield "Step 3: Add milk"
    yield "Step 4: Add sugar"
    yield "Step 5: Strain & serve"

# here the generator is different from a normal function
# as generators use 'yield' instead of 'return'
# they return a generator object  which can be iterated over to get each value one by one and store the last state in the memory
# example 
print(next(serve_chai()))  # Step 1: Boil water
# now the state is saved and next time it will start from where it left off
print(next(serve_chai()))  # Step 2: Add tea leaves
# but here we are calling the function again so it starts from the beginning
stall = serve_chai()
print(type(stall))  # <class 'generator'>
print(stall)
for step in stall:
    print(step)


