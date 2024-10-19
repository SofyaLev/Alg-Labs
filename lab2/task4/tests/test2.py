import time
import psutil
import random
from lab2.task4.src.binary_search import search_elements

test_nums2 = [random.randint(-10**9, 10**9+1) for _ in range(1, 10**5+1)]
test_targets2 = [random.randint(-10**9, 10**9+1) for _ in range(1, 10**5+1)]

start_time1 = time.perf_counter()
test1 = search_elements(test_nums2, test_targets2)
print(f'Время: {time.perf_counter() - start_time1} секунд')
print(f'Память: {psutil.Process().memory_info().rss / 1024**2} Мбайт')
