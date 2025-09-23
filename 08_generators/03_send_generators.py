def chai_customer():
    print("Welcome ! What chai would you like ?")
    order = yield
    while True:
        print(f"Preparing: {order}")
        # here we are stop and waiting for the next order so if we remove these yield statement it will run a infinite loop.
        order = yield

stall = chai_customer()
next(stall) # start the generator

stall.send("Masala Chai")
stall.send("Lemon Chai")
stall.send("Le Chai")