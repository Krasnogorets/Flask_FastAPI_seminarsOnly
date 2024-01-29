"""
Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
� Используйте асинхронный подход.
"""
import time
from pathlib import Path

import asyncio
import aiohttp


async def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        contents = f.read()
        print(f'{f.name} содержит {len(contents.split())} слов, {time.time() - start_time}seconds')


threads = []
start_time = time.time()


async def main():
    tasks = []
    dir_path = Path().cwd() / 'asyncio'
    file_paths = [file_path for file_path in dir_path.iterdir() if file_path.is_file()]
    for file_path in file_paths:
        task = asyncio.ensure_future(process_file(file_path))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
