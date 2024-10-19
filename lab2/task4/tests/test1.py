import time
import psutil
from lab2.task4.src.binary_search import search_elements

test_nums1 = [1, 5, 8, 12, 13]
test_targets1 = [8, 1, 23, 1, 11]

start_time1 = time.perf_counter()
test1 = search_elements(test_nums1, test_targets1)
print(f'Время: {time.perf_counter() - start_time1} секунд')
print(f'Память: {psutil.Process().memory_info().rss / 1024**2} Мбайт')
