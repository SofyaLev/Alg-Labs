import sys
import os
import psutil
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils import *

start_time = time.perf_counter()


def scarecrow_sort(n, k, array):
    for i in range(0, n-k):
        if array[i] > array[i+k]:
            array[i], array[i+k] = array[i+k], array[i]
    return "YES" if array == sorted(array) else "NO"


if __name__ == '__main__':
    data, massive = read_file(task=3)
    n, k = list(map(int, data.split()))
    array = list(map(int, massive.split()))
    scarecrow_sort = scarecrow_sort(n, k, array)
    write_output(3, scarecrow_sort)
    print(f'Время: {(time.perf_counter() - start_time):.6f} секунд')
    print(f'Память: {psutil.Process().memory_info().rss / 1024 ** 2} Мбайт')
