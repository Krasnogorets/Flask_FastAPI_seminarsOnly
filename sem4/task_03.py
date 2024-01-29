"""
Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
адреса.
� После загрузки данных нужно записать их в отдельные
файлы.
� Используйте асинхронный подход.
"""
import time
import asyncio
import aiohttp

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


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            filename = 'asyncio/' + url.replace('https://www.theyachtmarket.com/en/brokers', '') \
                .replace('.', '_').replace('/', '') + '.html'
            with open(filename, "w", encoding='utf-8') as f:
                f.write(text)
            print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


threads = []
start_time = time.time()
def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
