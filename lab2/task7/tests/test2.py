import time
import psutil
from lab2.task7.src.find_max_subarray import find_max_subarray

test_nums2 = [0]

start_time2 = time.perf_counter()
test2 = find_max_subarray(len(test_nums2), test_nums2)
print(f'Время: {time.perf_counter() - start_time2} секунд')
print(f'Память: {psutil.Process().memory_info().rss / 1024**2} Мбайт')
