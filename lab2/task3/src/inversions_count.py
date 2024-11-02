import sys
import os
import psutil
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils import read_file, write_output

def inversions_merge(array, temp_array, left, middle, right):
    i = left
    j = middle + 1
    k = left
    inversions_count = 0
    while i <= middle and j <= right:
        if array[i] <= array[j]:
            temp_array[k] = array[i]
            i += 1
        else:
            temp_array[k] = array[j]
            inversions_count += (middle - i + 1)
            j += 1
        k += 1
    while i <= middle:
        temp_array[k] = array[i]
        i += 1
        k += 1
    while j <= right:
        temp_array[k] = array[j]
        j += 1
        k += 1
    for i in range(left, right + 1):
        array[i] = temp_array[i]

    return inversions_count


def inversions_count(array, temp_array, left, right):
    counter = 0
    if left < right:
        middle = (left + right) // 2
        counter += inversions_count(array, temp_array, left, middle)
        counter += inversions_count(array, temp_array, middle+1, right)
        counter += inversions_merge(array, temp_array, left, middle, right)
    return counter


if __name__ == '__main__':
    _, massive = read_file(task=3)
    array = list(map(int, massive.split()))
    temp_array = [0] * len(array)
    inversions_count = inversions_count(array, temp_array, 0, len(array) - 1)
    write_output(3, str(inversions_count))
    print(f'Память: {psutil.Process().memory_info().rss / 1024 ** 2} Мбайт')
