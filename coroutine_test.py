import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

# 计算斐波那契数列的函数（这里使用递归）
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 异步函数，使用asyncio和ProcessPoolExecutor并行计算斐波那契数列
async def calculate_fibonacci_async(n):
    loop = asyncio.get_event_loop()

    # 使用ProcessPoolExecutor并行执行计算斐波那契数列的任务
    with ProcessPoolExecutor() as executor:
        result = await loop.run_in_executor(executor, fibonacci, n)


    return result

# 主函数
async def main():
    n = 35  # 计算斐波那契数列的第30个数
    tasks = [calculate_fibonacci_async(n) for _ in range(5)]  # 启动5个并发任务

    # 记录开始时间
    start_time = asyncio.get_event_loop().time()

    # 等待所有任务完成
    results = await asyncio.gather(*tasks)

    # 记录结束时间
    end_time = asyncio.get_event_loop().time()

    # 打印结果和总耗时时间
    for i, result in enumerate(results, 1):
        print(f"Task {i}: Fibonacci({n}) = {result}")

    total_time = end_time - start_time
    print(f"Total time with ProcessPoolExecutor: {total_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())