import time
import psutil
from lab2.task3.src.inversions_count import inversions_merge_sort

test_nums2 = [0]

start_time2 = time.perf_counter()
test2 = inversions_merge_sort(test_nums2, [0]*len(test_nums2), 0, len(test_nums2)-1)
print(f'Время: {time.perf_counter() - start_time2} секунд')
print(f'Память: {psutil.Process().memory_info().rss / 1024**2} Мбайт')
