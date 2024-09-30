import time
import psutil
from lab1.task4.src.task4 import linear_search

test_nums1 = [1, 2, 2, 3, 4, 15, 7]
test_v = 2

start_time1 = time.perf_counter()
test1 = linear_search(test_nums1, test_v)
print(f'Время: {time.perf_counter() - start_time1} секунд')
print(f'Память: {psutil.Process().memory_info().rss / 1024**2} Мбайт')
