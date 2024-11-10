import sys
import os
import psutil
import time
from lab3.task1.src.quick_sort import quick_sort
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils import *

start_time = time.perf_counter()


def hirsch_index(citations):
    n = len(citations)
    quick_sort(citations, 0, n-1)
    for h in range(n):
        if (n - h) <= citations[h]:
            return n - h
    return 0


if __name__ == '__main__':
    citations = read_file(task=5)[0]
    array = list(map(int, citations.split()))
    result = hirsch_index(array)
    output = str(result)
    write_output(5, output)
    print(f'Время: {(time.perf_counter() - start_time):.6f} секунд')
    print(f'Память: {psutil.Process().memory_info().rss / 1024 ** 2} Мбайт')
