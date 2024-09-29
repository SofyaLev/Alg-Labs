import time
import psutil
from lab1.task6.src.task6 import bubble_sort

test_nums1 = [31, 41, 59, 26, 41, 58]

start_time1 = time.perf_counter()
test1 = bubble_sort(len(test_nums1), test_nums1)
print(f'Время: {time.perf_counter() - start_time1} секунд')
print(f'Память: {psutil.Process().memory_info().rss / 1024**2:.2f} Мбайт')
