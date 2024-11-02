import sys
import os
import psutil
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils import read_file, write_output

def find_max_subarray(n, array):
    max_sum = 0
    left = 0
    right = 0
    current_sum = 0
    for i in range(n):
        if current_sum == 0:
            left = i
        current_sum += array[i]
        if current_sum < 0:
            current_sum = 0
        if current_sum > max_sum:
            max_sum = current_sum
            right = i
    return [max_sum, [left, right]]


if __name__ == '__main__':
    _, massive = read_file(task=7)
    array = list(map(int, massive.split()))
    result = find_max_subarray(len(array), array)
    output = str(result)
    write_output(7, output)
    print(f'Память: {psutil.Process().memory_info().rss / 1024 ** 2} Мбайт')
