import time
import psutil
import random
from lab2.task1.src.merge_sort import merge_sort

test_nums3 = sorted([random.randint(10**5, 10**9+1) for _ in range(1, 10**5+1)], reverse=True)

start_time3 = time.perf_counter()
test3 = merge_sort(test_nums3, 0, len(test_nums3)-1)
print(f'Время: {time.perf_counter() - start_time3} секунд')
print(f'Память: {psutil.Process().memory_info().rss / 1024**2} Мбайт')
