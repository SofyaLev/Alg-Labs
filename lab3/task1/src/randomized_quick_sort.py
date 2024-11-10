import sys
import os
import psutil
import time
import random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils import *

start_time = time.perf_counter()


def partition(A, l, r):
    x = A[l]
    j = l
    for i in range(l+1, r+1):
        if A[i] < x:
            j += 1
            A[j], A[i] = A[i], A[j]
    A[l], A[j] = A[j], A[l]
    return j


def randomized_quick_sort(A, l, r):
    if l < r:
        k = random.randint(l, r)
        A[l], A[k] = A[k], A[l]
        m = partition(A, l, r)
        randomized_quick_sort(A, l, m-1)
        randomized_quick_sort(A, m+1, r)


if __name__ == '__main__':
    _, massive = read_file(task=1)
    array = list(map(int, massive.split()))
    randomized_quick_sort(array, 0, len(array) - 1)
    write_output(1, ' '.join(map(str, array)))
    print(f'Время: {(time.perf_counter() - start_time):.6f} секунд')
    print(f'Память: {psutil.Process().memory_info().rss / 1024 ** 2} Мбайт')
