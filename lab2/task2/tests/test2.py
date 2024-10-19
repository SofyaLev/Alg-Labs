import time
import psutil
from lab2.task2.src.merge_sort_indexes import merge_sort_indexes

test_nums2 = [0]

start_time2 = time.perf_counter()
test2 = merge_sort_indexes(test_nums2, 0, len(test_nums2)-1)
print(f'Время: {time.perf_counter() - start_time2} секунд')
print(f'Память: {psutil.Process().memory_info().rss / 1024**2} Мбайт')
