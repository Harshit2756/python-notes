### The Problem

If you’re calling multiple slow APIs, like:

```python
def fetch_data(user):
    time.sleep(3)
    print(f"Data fetched for {user}!")

def main():
    fetch_data("user1")
    fetch_data("user2")
    fetch_data("user3")
    print("All done!")

main()
```

Each one waits for the other to finish.
⏳ If each takes 1s → total = 3s
But in reality, network calls mostly wait on I/O — so we could’ve done them concurrently in ~1s.

### Enter Asyncio

That’s where asyncio shines: it pauses a task while it’s waiting and lets another run, instead of blocking.

#### Event Loop

### How the Event Loop Works (Step-by-Step)

1. **Initialization**: The event loop starts running and maintains a queue of tasks (coroutines) that are either ready to run or waiting for something (like I/O, timers, etc.).
2. **Pick a Task to Run**: The loop picks the next coroutine from the queue that’s in a ready state — meaning it’s not currently waiting for an I/O or sleep to complete.
3. **Execute Until await**: The event loop runs that coroutine until it hits an await keyword. When the coroutine reaches await something, it’s basically saying:
   “Pause me here — I’ll come back when something is done.”
4. **Register the Awaited Operation**: The loop doesn’t just stop — it registers the awaited operation (like reading a socket, fetching data, sleeping, etc.) with the underlying OS or I/O system. That way, the event loop knows when the operation is complete (via callback or signal).
5. **Suspend and Move On**: While that coroutine is waiting, the event loop suspends it and moves on to the next ready coroutine in the queue. This is where concurrency happens — many coroutines make progress without blocking each other.
6. **Resume Completed Tasks**: When the awaited operation finishes, the event loop gets notified. The corresponding coroutine is marked as ready again and placed back into the queue.
7. **Repeat the Cycle**: The loop continues picking ready coroutines, executing them until their next await, suspending, resuming — over and over. This keeps going until all tasks are completed or the loop is stopped.

#### async def

- declares a coroutine (special function that can be paused)

#### await (pause and yeilding not waiting)

| Concept        | Waiting                          | Yielding                               
| -------------- | -------------------------------- | -------------------------------------- 
| Type           | Blocking                         | Non-blocking                           
| CPU usage      | Idle                             | Always doing something useful          
| Who manages it | The interpreter (just waits)     | The event loop (schedules other tasks) 
| Efficiency     | Wastes time                      | Efficient multitasking                 
| Keyword        | **time.sleep()** / blocking call | **await** + async function             

- pauses execution until the result is ready.

example:

```python
import asyncio

async def taskA():
    print("A: Started")
    await asyncio.sleep(2)
    print("A: Finished after 2s")

async def taskB():
    print("B: Started")
    await asyncio.sleep(1)
    print("B: Finished after 1s")

async def main():
    print("Main: Starting tasks...")
    
    # Start both tasks concurrently
    asyncio.create_task(taskA())
    asyncio.create_task(taskB())
    
    print("Main: All tasks started!")
    
    # Let the event loop keep running for 3 seconds
    await asyncio.sleep(3)
    
    print("Main: Exiting")

# Run the event loop
asyncio.run(main())
```
Output:
```
Main: Starting tasks...
A: Started
B: Started
Main: All tasks started!
B: Finished after 1s
A: Finished after 2s
Main: Exiting
```

#### asyncio

Python’s built-in library that provides:

- The event loop (the brain that manages async tasks)
- Async utilities like:
  - asyncio.run() — runs your main coroutine
  - asyncio.gather() — runs multiple coroutines concurrently
  - asyncio.sleep() — async-friendly sleep (non-blocking)
  - asyncio.create_task() — schedules coroutines to run in parallel
