import time
import psutil
from lab1.task2.src.task2 import insertion_sort

test_nums1 = [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]

start_time1 = time.perf_counter()
test1 = insertion_sort(len(test_nums1), test_nums1)
print(f'Время: {time.perf_counter() - start_time1} секунд')
print(f'Память: {psutil.Process().memory_info().rss / 1024**2} Мбайт')