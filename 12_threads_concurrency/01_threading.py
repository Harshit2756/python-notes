# Concurrency : 
# - doing multiple things at once as like context switching
# - here the one process is not waiting for another process to complete
# => Threading (thread)
# => asyncio
 
import threading
import time

def take_order():
    for i in range(1,4):
        print(f"Taking order for #{i}")
        time.sleep(2)

def brew_chai():
    for i in range(1,4):
        print(f"Brewing chai for #{i}")
        time.sleep(3)

# create threads
order_thread = threading.Thread(target=take_order)
brew_thread = threading.Thread(target=brew_chai)

order_thread.start()
brew_thread.start()

#  wait for both to finish
order_thread.join()
brew_thread.join()

print(f"All orders taken and chai brewed.")


