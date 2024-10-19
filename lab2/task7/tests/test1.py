import time
import psutil
from lab2.task7.src.find_max_subarray import find_max_subarray

test_nums1 = [1, 8, 2, 10]

start_time1 = time.perf_counter()
test1 = find_max_subarray(len(test_nums1), test_nums1)
print(f'Время: {time.perf_counter() - start_time1} секунд')
print(f'Память: {psutil.Process().memory_info().rss / 1024**2} Мбайт')
