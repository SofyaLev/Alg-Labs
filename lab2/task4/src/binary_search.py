import sys
import os
import psutil
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils import read_file, write_output

def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1

def search_elements(array, targets):
    result = []
    for target in targets:
        index = binary_search(array, target)
        result.append(index)
    return result


if __name__ == '__main__':
    _, massive, _,  targets = read_file(task=4)
    array = list(map(int, massive.split()))
    targets = list(map(int, targets.split()))
    result = search_elements(array, targets)
    write_output(4, ' '.join(list(map(str, result))))
    print(f'Память: {psutil.Process().memory_info().rss / 1024 ** 2} Мбайт')
