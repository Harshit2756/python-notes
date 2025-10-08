import asyncio
import threading
import time

def background_worker():
    while True:
        time.sleep(1)
        print(f"Logging the system health")

async def fetch_orders():
    await asyncio.sleep(3)
    print(" order fetched")
# A daemon thread runs in the background, and the main Python program will not wait for it to finish. Once the non-daemon threads (in this case, the asyncio.run thread) finish, the program exits, killing the daemon thread instantly.
# 
threading.Thread(target=background_worker, daemon=True).start()

asyncio.run(fetch_orders())