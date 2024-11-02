import sys
import os
import psutil
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils import read_file, write_output

def majority_element(array):
    def find_candidate(array):
        count = 0
        candidate = None
        for number in array:
            if count == 0:
                candidate = number
                count = 1
            elif number == candidate:
                count += 1
            else:
                count -= 1

        return candidate

    def is_majority(array, candidate):
        count = sum(1 for number in array if number == candidate)
        return count > len(array) // 2

    candidate = find_candidate(array)

    if is_majority(array, candidate):
        return 1
    else:
        return 0


if __name__ == '__main__':
    _, massive = read_file(task=5)
    array = list(map(int, massive.split()))
    result = majority_element(array)
    output = str(result)
    write_output(5, output)
    print(f'Память: {psutil.Process().memory_info().rss / 1024 ** 2} Мбайт')
