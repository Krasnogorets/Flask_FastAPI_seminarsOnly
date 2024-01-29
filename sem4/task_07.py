"""
Напишите программу на Python, которая будет находить
сумму элементов массива из 1000000 целых чисел.
� Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
� Массив должен быть заполнен случайными целыми числами
от 1 до 100.
� При решении задачи нужно использовать многопоточность,
многопроцессорность и асинхронность.
� В каждом решении нужно вывести время выполнения
вычислений.
"""
import multiprocessing
import random
import time
import threading
from multiprocessing import Process, Pool
import asyncio

arr = [0] * 10_000_000
result = 0


def create_array_flat(start, stop):  # синхронный процесс
    start_time = time.time()
    global arr
    for i in range(start, stop):
        arr[i] = random.randint(1, 101)
    print(f'синхронный процесс занял{time.time() - start_time} seconds, sum={sum(arr)}')


def create_array(start, stop):  # многопотоковый
    global result
    global arr
    sum_ = 0
    for i in range(start, stop):
        arr[i] = random.randint(1, 101)
        sum_ += arr[i]
    result += sum_


def create_array_proc(start, stop, result):  # процессный
    global arr
    sum_ = 0
    for i in range(start, stop):
        arr[i] = random.randint(1, 101)
        sum_ += arr[i]
    with result:
        result.value += sum_


async def create_array_(start, stop):  # асинхронный
    global result
    global arr
    sum_ = 0
    for i in range(start, stop):
        arr[i] = random.randint(1, 101)
        sum_ += arr[i]
    result += sum_


def treading(arr1):
    threads = []
    start_time = time.time()
    threads_count = 50
    step = len(arr1) // threads_count
    for i in range(0, len(arr1), step):
        stop = i + step
        # print(i, stop)
        thread = threading.Thread(target=create_array, args=[i, stop])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f'многопотоковый занял {time.time() - start_time} seconds, sum={result}')


async def main():
    global arr
    tasks = []
    start_time = time.time()
    threads_count = 50
    step = len(arr) // threads_count
    for i in range(0, len(arr), step):
        stop = i + step
        # print(i, stop)
        task = asyncio.ensure_future(create_array_(i, stop))
        tasks.append(task)
    await asyncio.gather(*tasks)
    print(f'асинхронный занял {time.time() - start_time} seconds, sum={result}')


if __name__ == '__main__':
    print('каждый вариант генерирует свой набор случайных чисел, т.к. именно генерация занимает основное время, '
          'а не суммирование')
    create_array_flat(0, 10_000_000)
    print(f'checking sum={sum(arr)}')
    treading(arr)
    print(f'checking sum={sum(arr)}')
    result_proc = multiprocessing.Value('i', 0)

    processes = []
    start_time = time.time()
    process_count = 10
    step = len(arr) // process_count
    for i in range(0, len(arr), step):
        stop = i + step
        # print(i, stop)
        process = Process(target=create_array_proc, args=(i, stop, result_proc,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()

    print(f'многопроцессный занял{time.time() - start_time} seconds, sum={result_proc.value}')
    print(f'checking sum={sum(arr)}')
    result = 0
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(f'checking sum={sum(arr)}')
