import sys
import os
import psutil
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils import *

start_time = time.perf_counter()


def qsort(a, left, right):
    key = a[(left+right)//2]
    i = left
    j = right
    while i <= j:
        while a[i] < key:
            i += 1
        while a[j] > key:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    if left < j:
        qsort(a, left, j)
    if i < right:
        qsort(a, i, right)
    return a


def anti_quick_sort(n):
    a = [i+1 for i in range(n)]
    for i in range(2, len(a)):
        a[i], a[i//2] = a[i//2], a[i]
    return a


if __name__ == '__main__':
    data = read_file(task=2)[0]
    n = int(data)
    result = anti_quick_sort(n)
    write_output(2, ' '.join(list(map(str, result))))
    print(f'Время: {(time.perf_counter() - start_time):.6f} секунд')
    print(f'Память: {psutil.Process().memory_info().rss / 1024 ** 2} Мбайт')
