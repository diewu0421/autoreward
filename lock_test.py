import time
import random
from concurrent.futures import ThreadPoolExecutor
from threading import RLock


class Account(object):
    """银行账户"""

    def __init__(self):
        self.balance = 0.0  # 表示现有余额
        self.lock = RLock()

    def deposit(self, save_money):
        self.lock.acquire()        # 获得锁

        new_balance = self.balance + save_money  # 新的余额等于旧的余额+存进去的money
        time = random.uniform(0.01, 0.9)
        print("time = ", time)
        time.sleep(time)   # 模拟一个0.01~0.9s的随机延时
        self.balance = new_balance			# 更新现有余额

        self.lock.release()		# 释放锁

account = Account()  # 实例化一个银行账户类

pool = ThreadPoolExecutor(5)
for _ in range(20):
    pool.submit(account.deposit, 100)

print(account.balance)
