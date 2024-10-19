import time
import random
import psutil
from lab2.task1.src.merge_sort import merge_sort

test_nums2 = sorted(random.randint(10**5, 10**9+1) for _ in range(1, 10**5+1))

start_time2 = time.perf_counter()
test2 = merge_sort(test_nums2, 0, len(test_nums2)-1)
print(f'Время: {time.perf_counter() - start_time2} секунд')
print(f'Память: {psutil.Process().memory_info().rss / 1024**2} Мбайт')
