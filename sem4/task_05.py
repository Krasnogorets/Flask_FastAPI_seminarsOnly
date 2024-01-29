"""
Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
� Используйте процессы.
"""
import time
from multiprocessing import Process
from pathlib import Path


def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        contents = f.read()
        print(f'{f.name} содержит {len(contents.split())} слов, {time.time() - start_time}seconds')


processes = []
start_time = time.time()

if __name__ == '__main__':
    dir_path = Path().cwd() / 'processing'
    file_paths = [file_path for file_path in dir_path.iterdir() if file_path.is_file()]
    for file_path in file_paths:
        process = Process(target=process_file, args=(file_path,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
