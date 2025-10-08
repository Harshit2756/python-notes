import asyncio
import time
from concurrent.futures import ThreadPoolExecutor
# Execute computations asynchronously using threads or processes.

def check_stock(item):
    print(f"Checking {item} in store....")
    time.sleep(3) # Blocking operation(waiting)
    return f"{item} stock:42"

async def main():
    loop = asyncio.get_running_loop()  # got the currect event loop
    with ThreadPoolExecutor() as pool: # creates a pool of worker threads
        result = await loop.run_in_executor(pool, check_stock, "Masala Chai") 
        # The check_stock function runs synchronously in the separate thread.
        # The event loop is not blocked; it can continue processing other tasks (though in this simple example, there are none).
        # The main coroutine awaits the result. When the thread completes the check_stock function after 3 seconds, the result is returned to the event loop, and the main coroutine resumes execution.
        print(result)

asyncio.run(main())