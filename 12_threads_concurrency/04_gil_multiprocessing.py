# Using multiprocessing to bypass GIL for CPU-bound tasks
# In multiprocessing, each process has its own Python interpreter and memory space, so the GIL does not prevent multiple processes from executing Python code simultaneously.

from multiprocessing import Process
import time

def crunch_number(name):
    print(f"Started the count process in {name}...")
    # here count is the same variable for both processes but since they have their own memory space so no interference will happen. and mutex is not required here.
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"Ended the count process in {name}...")

# The if __name__ == "__main__": is necessary as the process don't know where to start executing the code from.whereas in threading it starts from the top. 
if __name__ == "__main__":
    start = time.time()

    p1 = Process(target=crunch_number, args=("Process-1",))
    p2 = Process(target=crunch_number, args=("Process-2",))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()

    print(f"Total time with multi-processing is {end - start:.2f} seconds")
