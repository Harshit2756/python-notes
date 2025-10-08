import asyncio
import time
from concurrent.futures import ProcessPoolExecutor


def encrpty(data):
    return f"lock: {data[::-1]}"

async def main():
    loop = asyncio.get_running_loop()  # got the currect event loop
    with ProcessPoolExecutor() as pool: # creates a pool of worker process
        result = await loop.run_in_executor(pool, encrpty, "cc_12453") 
        # The encrpty function runs synchronously in the separate process.
        # The event loop is not blocked; it can continue processing other tasks (though in this simple example, there are none).
        # The main coroutine awaits the result. When the process completes the check_stock function after 3 seconds, the result is returned to the event loop, and the main coroutine resumes execution.
        print(f"{result}")

asyncio.run(main())