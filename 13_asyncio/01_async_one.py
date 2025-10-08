import asyncio

async def brew_chai():
    print("Brwing chai....")
    await asyncio.sleep(2)
    print("Chai is ready")

# Runs the event loop and executes the coroutine
asyncio.run(brew_chai())