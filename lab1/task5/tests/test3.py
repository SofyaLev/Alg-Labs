import time
import psutil
import random
from lab1.task5.src.task5 import selection_sort

test_nums3 = [random.randint(-10**9, 10**9+1) for _ in range(1, 10**3+1)]

start_time3 = time.perf_counter()
test2 = selection_sort(len(test_nums3), test_nums3)
print(f'Время: {time.perf_counter() - start_time3} секунд')
print(f'Память: {psutil.Process().memory_info().rss / 1024**2} Мбайт')