import sys
import os
import psutil
import time
import random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils import *

start_time = time.perf_counter()


def partition3(A, l, r):
    x = A[l]
    m1 = l
    m2 = r
    i = l
    while i <= m2:
        if A[i] < x:
            A[m1], A[i] = A[i], A[m1]
            m1 += 1
            i += 1
        elif A[i] > x:
            A[i], A[m2] = A[m2], A[i]
            m2 -= 1
        else:
            i += 1
    return m1, m2


def randomized_quick_sort_p3(A, l, r):
    if l < r:
        k = random.randint(l, r)
        A[l], A[k] = A[k], A[l]
        m1, m2 = partition3(A, l, r)
        randomized_quick_sort_p3(A, l, m1-1)
        randomized_quick_sort_p3(A, m2+1, r)


if __name__ == '__main__':
    _, massive = read_file(task=1)
    array = list(map(int, massive.split()))
    randomized_quick_sort_p3(array, 0, len(array) - 1)
    write_output(1, ' '.join(map(str, array)))
    print(f'Время: {(time.perf_counter() - start_time):.6f} секунд')
    print(f'Память: {psutil.Process().memory_info().rss / 1024 ** 2} Мбайт')
