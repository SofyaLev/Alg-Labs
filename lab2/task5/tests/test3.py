import time
import psutil
import random
from lab2.task5.src.majority_element import majority_element

test_nums3 = [random.randint(-10**9, 10**9+1) for _ in range(1, 10**5+1)]

start_time3 = time.perf_counter()
test2 = majority_element(test_nums3)
print(f'Время: {time.perf_counter() - start_time3} секунд')
print(f'Память: {psutil.Process().memory_info().rss / 1024**2} Мбайт')