import time
import psutil
from lab2.task5.src.majority_element import majority_element

test_nums2 = [0]

start_time2 = time.perf_counter()
test2 = majority_element(test_nums2)
print(f'Время: {time.perf_counter() - start_time2} секунд')
print(f'Память: {psutil.Process().memory_info().rss / 1024**2} Мбайт')
