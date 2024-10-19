import time
import psutil
from lab2.task1.src.merge_sort import merge_sort

test_nums1 = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]

start_time1 = time.perf_counter()
test1 = merge_sort(test_nums1, 0, len(test_nums1)-1)
print(f'Время: {time.perf_counter() - start_time1} секунд')
print(f'Память: {psutil.Process().memory_info().rss / 1024**2} Мбайт')
