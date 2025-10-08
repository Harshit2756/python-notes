import asyncio
import time
async def brew_chai(name):
    print(f"Brewing {name} chai....")
    # await asyncio.sleep(3) # here it will take 3 sec as it is waiting in a non blocking way
    time.sleep(3) # here it will take 9 seconds to complete the task
    print(f"{name} is ready")

async def main():
    await asyncio.gather(
        brew_chai("Lemon"),
        brew_chai("Masala"),
        brew_chai("Ginger")
    )

asyncio.run(main())