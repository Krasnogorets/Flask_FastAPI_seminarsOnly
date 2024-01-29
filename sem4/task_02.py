"""
Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
адреса.
� После загрузки данных нужно записать их в отдельные
файлы.
� Используйте процессы.
"""
from multiprocessing import Process, Pool
import requests
import time

urls = ['https://www.theyachtmarket.com/en/brokers/30274/acaster-marine/office/54279/acaster-marine/',
        'https://www.theyachtmarket.com/en/brokers/46481/adamson-international/office/66961/adamson-international/',
        'https://www.theyachtmarket.com/en/brokers/5366/ancasta-international-boat-sales/office/47533/ancasta-ancasta-multihulls/',
        'https://www.theyachtmarket.com/en/brokers/5366/ancasta-international-boat-sales/office/49135/ancasta-ancasta-raceboats/',
        'https://www.theyachtmarket.com/en/brokers/5366/ancasta-international-boat-sales/office/154/ancasta-beneteau-yachts/',
        'https://www.theyachtmarket.com/en/brokers/5366/ancasta-international-boat-sales/office/167/ancasta-brighton/',
        'https://www.theyachtmarket.com/en/brokers/5366/ancasta-international-boat-sales/office/46217/ancasta-chichester/',
        'https://www.theyachtmarket.com/en/brokers/5366/ancasta-international-boat-sales/office/60906/ancasta-cowes/',
        'https://www.theyachtmarket.com/en/brokers/5366/ancasta-international-boat-sales/office/51500/ancasta-dartmouth/',
        'https://www.theyachtmarket.com/en/brokers/5366/ancasta-international-boat-sales/office/156/ancasta-falmouth/',
        'https://www.theyachtmarket.com/en/brokers/5366/ancasta-international-boat-sales/office/18444/ancasta-international-boat-sales/',
        'https://www.theyachtmarket.com/en/brokers/5366/ancasta-international-boat-sales/office/48388/ancasta-london/'
        ]


def download(url):
    response = requests.get(url)
    filename = 'processing/' + url.replace('https://www.theyachtmarket.com/en/brokers',
                                           '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
        print(f"Downloaded {url} in {time.time() - start_time:.2f}seconds")


processes = []
start_time = time.time()

if __name__ == '__main__':
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
