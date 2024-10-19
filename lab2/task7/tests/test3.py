import time
import psutil
import random
from lab2.task7.src.find_max_subarray import find_max_subarray

test_nums3 = sorted(random.randint(10**5, 10**9+1) for _ in range(1, 10**5+1))

start_time3 = time.perf_counter()
test3 = find_max_subarray(len(test_nums3), test_nums3)
print(f'Время: {time.perf_counter() - start_time3} секунд')
print(f'Память: {psutil.Process().memory_info().rss / 1024**2} Мбайт')
