from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

import asyncio
import time
import easyocr

from pathlib import Path


async def startOcr(args):
    print("start ocr")
    reader = args[0]
    path = Path("test.png")
    while True:
        if path.exists():
            print("path exist")
            ret = reader.readtext(path, detail=0)
            if ret:
                print("ret = ", ret)
            path.unlink()
        path = Path("test2.bmp")
        await asyncio.sleep(0.5)


async def main():
    reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)
    print("main reader")
    # ret = reader.readtext("test.png", detail=0)
    # print(ret)
    # with ThreadPoolExecutor() as pool:
        # pool.submit(startOcr, reader)
        # await loop.run_in_executor(pool, startOcr, reader)
    path = Path("test.png")
    while True:
        if path.exists():
            ret = reader.readtext(str(path), detail=0)
            if ret:
                print("ret = ", ret)

            path.unlink()
        path = Path("test2.bmp")
        await asyncio.sleep(0.5)


async def start():
    tasks = [main(), ]
    results = await asyncio.gather(*tasks)
    print("results", results)


asyncio.run(start())
