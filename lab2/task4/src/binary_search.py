from lab2.utils import read_from_file, write_in_file, measuring


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
    data = read_from_file('../txtf/input.txt')

    n = data[0]
    array = data[1:n+1]
    k = data[n+1]
    targets = data[k:]
    result = search_elements(array, targets)

    write_in_file('../txtf/output.txt', result)

    measuring(search_elements, array, targets)
