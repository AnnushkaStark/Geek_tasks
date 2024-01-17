import requests
from threading import Thread
from multiprocessing import Process
import time
import os


urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        'https://skillfactory.ru/',
        #'https://skillbox.ru/',
        'https://pstu.ru/'
        ]



def checkUrls():
    folder = 'data_task_2'
    if not os.path.exists(folder):
        os.mkdir(folder)
    for index, url in enumerate(urls):
        name = os.path.join(folder, f'name_{index}.txt')
        download_data(url, name)
        


def download_data(url, filename):
    
    response = requests.get(url)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)


if __name__ =='__main__':
    start_time = time.time()

    checkUrls()
     
    print(time.time() - start_time)

    threads = []
    start_time = time.time()
    folder = 'data_task_1'
    if not os.path.exists(folder):
        os.mkdir(folder)


    for index, url in enumerate(urls):
        name = os.path.join(folder, f'name_{index}.txt')
        thread = Thread(target=download_data, args=[url, name])
        threads.append(thread)
        
    
    for thread in threads:
        thread.start()


    for thread in threads:
        thread.join()
    print(time.time() - start_time)



    proceses = []
    start_time = time.time()
    folder = 'data_task_1'
    if not os.path.exists(folder):
        os.mkdir(folder)


    for index, url in enumerate(urls):
        name = os.path.join(folder, f'name_{index}.txt')
        process = Process(target=download_data, args=[url, name])
        proceses.append(process)
        
   
    for process in proceses:
        process.start()

    for process in proceses:
        process.join()


    print(time.time() - start_time)


