import asyncio
import random
import aiohttp
import time
import os

img_URL = "https://picsum.photos/300"

async def download(session, task_id):
    async with session.get(img_URL) as response:
        img_bytes = await response.read()

        current_time = time.time()
        filename = f"images/img_{current_time}_{task_id}.jpg"
        with open(filename, "wb") as file:
            file.write(img_bytes)

        print(f"Task {task_id}, saved image {filename}")

async def seq(amount):
    print("Sequential download")
    start = time.time()

    async with aiohttp.ClientSession() as session:
        for i in range(amount):
            await download(session, i)

    end_time = time.time()
    print(f"Total sequential download time: {end_time - start:.2f} seconds")

async def conc(amount):
    print("Concurrent download")
    start = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(amount):
            tasks.append(asyncio.create_task(download(session, i)))
        await asyncio.gather(*tasks)

    end_time = time.time()
    print(f"Total concurrent download time: {end_time - start:.2f} seconds")

async def main():
    folder_path = os.path.expanduser("~/PycharmProjects/ServerProgramming/images")
    os.makedirs(folder_path, exist_ok=True)

    photo_amount = random.randint(10, 50)

    await seq(photo_amount)
    print("===========================")
    await conc(photo_amount)

if __name__ == "__main__":
    asyncio.run(main())