import asyncio
import random

async def task(task_id):
    delay = random.uniform(0.1, 3.0)
    print(f"Task {task_id} requires {delay:.2f} seconds")
    await asyncio.sleep(delay)
    print(f"Task {task_id} completed in {delay:.2f} seconds")

async def main():
    print("Starting batch of tasks with 2 second timeout")
    tasks = []
    for i in range(5):
        tasks.append(asyncio.create_task(task(i)))
    try:
        await asyncio.wait_for(asyncio.gather(*tasks), timeout=2)
        print("All tasks complete before timeout!")
    except asyncio.TimeoutError:
        print("Timeout! Tasks didn't finish on time")

if __name__ == "__main__":
    asyncio.run(main())