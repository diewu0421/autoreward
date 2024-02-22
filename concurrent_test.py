from random import random, randint

import time

from threading import Thread


class DownloadThread(Thread):
    def __init__(self, file_name):
        self.file_name = file_name
        super().__init__()

    def run(self):
        s = time.time()
        print("start ", self.file_name)
        time.sleep(randint(1, 5))
        print("download complete ", self.file_name, "spendTime ", time.time() - start)


files = ("简单爱", "夜的第七章", "说好的幸福呢")

download_threads = (DownloadThread(file) for file in files)

start = time.time()
for thread in download_threads:
    thread.start()

for thread in download_threads:
    thread.join()

print("total time ", time.time() - start)
