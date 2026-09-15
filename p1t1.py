import asyncio
import random
import time

async def work():
    delay = random.randint(1, 3)
    await asyncio.sleep(delay)
    print(f"Task finished after {delay} seconds")

async def seq_func():
    print("Sequential execution:")
    start_time = time.time()
    for i in range(5):
        await work()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.2f} seconds\n")

async def conc_func():
    print("Concurrent execution:")
    start_time = time.time()
    tasks = []
    for i in range(5):
        tasks.append(asyncio.create_task(work()))
    await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.2f} seconds\n")

async def main():
    await seq_func()
    print("===========================\n")
    await conc_func()
    return 0

if __name__ == "__main__":
    asyncio.run(main())