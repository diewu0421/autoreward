from concurrent.futures import ThreadPoolExecutor


import random

import  time

def download(url):
    print("start, url ", url)
    time.sleep(random.randint(1,4))
    return random.randint(100, 200)


executor = ThreadPoolExecutor(5)

urls = [f"http://www.baidu.com/{index}" for index in range(0, 20)]


def on_complete(response):
    print("返回值： ", response.result())

for url in urls:
    feature =executor.submit(download, url)
    print("feature", feature)
    feature.add_done_callback(on_complete)

executor.shutdown()


print("download over")

