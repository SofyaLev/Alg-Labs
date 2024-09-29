import time
import psutil
from lab1.task1.src.task1 import insertion_sort

test_nums2 = [0]

start_time2 = time.perf_counter()
test2 = insertion_sort(len(test_nums2), test_nums2)
print(f'Время: {time.perf_counter() - start_time2} секунд')
print(f'Память: {psutil.Process().memory_info().rss / 1024**2:.2f} Мбайт')
