"""
Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
� Используйте потоки.

"""
from pathlib import Path
import os
import time

import threading


def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        contents = f.read()
        lst = contents.split()
        # for item in enumerate(lst, 1):
        #     print(item)
        # do some processing with the file contents
        print(f'{f.name} содержит {len(contents.split())} слов, {time.time() - start_time}seconds')


# threads = []
start_time = time.time()
dir_path = Path().cwd() / 'threading'
# dir_path = Path('/threading')
# dir_path = Path('.')
file_paths = [file_path for file_path in dir_path.iterdir() if file_path.is_file()]
threads = [threading.Thread(target=process_file, args=[file_path]) for file_path in file_paths]
# threads.append(*thread)
for thread in threads:
    thread.start()


for thread in threads:
    thread.join()
# if __name__ == '__main__':
#     process_file('threading/5366ancasta-international-boat-salesoffice154ancasta-beneteau-yachts.html')
#     process_file('threading/5366ancasta-international-boat-salesoffice156ancasta-falmouth.html')
