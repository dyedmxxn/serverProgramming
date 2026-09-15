import asyncio
import random
import time

async def task(task_id, semaphore):
    async with semaphore:
        print(f"Task {task_id} has started")
        delay = random.uniform(0.1, 1.0)
        await asyncio.sleep(delay)
        print(f"Task {task_id} has been completed in {delay:.2f} seconds")

async def main():
    semaphore = asyncio.Semaphore(5)
    tasks = []
    for i in range(50):
        tasks.append(asyncio.create_task(task(i, semaphore)))
    print("Starting batch of 50 tasks")
    start = time.time()
    await asyncio.gather(*tasks)
    end = time.time()
    print(f"Finished batch of tasks in {end - start:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())