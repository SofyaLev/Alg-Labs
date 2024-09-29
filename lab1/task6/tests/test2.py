import time
import psutil
import random
from lab1.task6.src.task6 import bubble_sort

test_nums2 = [random.randint(-10**9, 10**9+1) for _ in range(1, 10**3+1)]

start_time2 = time.perf_counter()
test2 = bubble_sort(len(test_nums2), test_nums2)
print(f'Время: {time.perf_counter() - start_time2} секунд')
print(f'Память: {psutil.Process().memory_info().rss / 1024**2:.2f} Мбайт')