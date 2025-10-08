# Race:
# because the operating system constantly switches between threads, a thread can be interrupted at any point between these steps.

# Imagine chai_stock is 100:

# Thread 1 Action |	Thread 2 Action | chai_stock | Result
# Reads 100		  |                 |  100	     | T1 prepares to write 101.
# (Interrupted)	  | Reads 100       |  100       | T2 prepares to write 101.
#                 | Writes 101      |  101	     | T2 finishes its update.
# Writes 101      |                 |  101	     | T1 finishes, overwriting T2's work!
# In this scenario, two separate increment operations only resulted in the stock increasing by one, causing a lost update.


import threading
chai_stock = 0

def restock():
    global chai_stock
    for _ in range(100000):
        chai_stock += 1

threads =  [ threading.Thread(target=restock) for _ in range(2)]

for t in threads:t.start()
for t in threads: t.join()

print("Chai stock: ", chai_stock)