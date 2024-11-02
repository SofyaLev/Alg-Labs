import sys
import os
import psutil
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils import read_file, write_output

def merge(array, left, middle, right):
    l_array = array[left:middle+1] + [float('inf')]
    r_array = array[middle+1:right+1] + [float('inf')]
    i = j = 0
    for k in range(left, right+1):
        if l_array[i] <= r_array[j]:
            array[k] = l_array[i]
            i += 1
        else:
            array[k] = r_array[j]
            j += 1


def merge_sort(array, left, right):
    if left < right:
        middle = (left + right) // 2
        merge_sort(array, left, middle)
        merge_sort(array, middle+1, right)
        merge(array, left, middle, right)
        return array


if __name__ == '__main__':
    _, massive = read_file(task=1)
    array = list(map(int, massive.split()))
    merge_sort(array, 0, len(array) - 1)
    write_output(1, ' '.join(map(str, array)))
    print(f'Память: {psutil.Process().memory_info().rss / 1024 ** 2} Мбайт')
