import sys
import os
import psutil
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils import *

start_time = time.perf_counter()


def partition(A, l, r):
    x = A[l][0]
    j = l
    for i in range(l+1, r+1):
        if A[i][0] < x:
            j += 1
            A[j], A[i] = A[i], A[j]
    A[l], A[j] = A[j], A[l]
    return j


def quick_sort(A, l, r):
    if l < r:
        j = partition(A, l, r)
        quick_sort(A, l, j-1)
        quick_sort(A, j+1, r)


def closest_points(array, k):
    points = []
    for cord in array:
        x, y = cord
        distance = int((x**2 + y**2)**0.5)
        points.append([distance, [x, y]])
    quick_sort(points, 0, len(points)-1)
    return [elem[1] for elem in points[:k]]


if __name__ == '__main__':
    data = read_file(task=8)
    n, k = list(map(int, data[0].split()))
    array = [list(map(int, cord.split())) for cord in data[1:]]
    result = closest_points(array, k)
    write_output(8, result)
    print(f'Время: {(time.perf_counter() - start_time):.6f} секунд')
    print(f'Память: {psutil.Process().memory_info().rss / 1024 ** 2} Мбайт')
