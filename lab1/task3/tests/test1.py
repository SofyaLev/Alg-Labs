import time
import psutil
from lab1.task3.src.task3 import insertion_sort_swap

test_nums1 = [31, 41, 59, 26, 41, 58]

start_time1 = time.perf_counter()
test1 = insertion_sort_swap(len(test_nums1), test_nums1)
print(f'Время: {time.perf_counter() - start_time1} секунд')
print(f'Память: {psutil.Process().memory_info().rss / 1024**2:.2f} Мбайт')
