# Race(a condition where two or more threads can access shared data and they try to change it at the same time) conditions are avoided by GIL
# GIL is necessary because Classic Python's memory management is not thread-safe. Without the GIL, multiple threads could simultaneously modify Python objects, leading to data corruption and crashes.
# Global Interpreter Lock (GIL) is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once.
# This means that in a multi-threaded Python program, even if multiple threads are running, only one thread can execute Python code at a time.

import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} started brewing...")
    # so here count is the same variable for both threads so gil will allow only one thread to execute this block at a time so like context switching will happen.
    count = 0 # Simulating a CPU-bound task
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing...")

thread1 = threading.Thread(target=brew_chai, name="Barista-1")
thread2 = threading.Thread(target=brew_chai, name="Barista-2")

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()

print(f"total time taken: {end - start:.2f} seconds")