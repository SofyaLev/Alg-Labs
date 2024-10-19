import time
import psutil
from lab2.task5.src.majority_element import majority_element

test_nums1 = [2, 3, 9, 2, 2]

start_time1 = time.perf_counter()
test1 = majority_element(test_nums1)
print(f'Время: {time.perf_counter() - start_time1} секунд')
print(f'Память: {psutil.Process().memory_info().rss / 1024**2} Мбайт')
