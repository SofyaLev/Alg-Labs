from utils import read, write


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


def main():
    write(end='')
    data = [list(line) for line in read(type_convert=int)]
    array = data[1]
    targets = data[3]
    write(*search_elements(array, targets), to_end=True)


if __name__ == '__main__':
    main()
