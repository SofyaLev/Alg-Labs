from lab2.utils import read_from_file, write_in_file, measuring


def merge_indexes(array, left, middle, right):
    l_array = array[left:middle+1] + [float('inf')]
    r_array = array[middle+1:right+1] + [float('inf')]
    i = j = 0
    print(f'Indexes: {left+1}, {right+1}. Elements: {array[left]}, {array[right]}')
    for k in range(left, right+1):
        if l_array[i] <= r_array[j]:
            array[k] = l_array[i]
            i += 1
        else:
            array[k] = r_array[j]
            j += 1


def merge_sort_indexes(array, left, right):
    if left < right:
        middle = (left + right) // 2
        merge_sort_indexes(array, left, middle)
        merge_sort_indexes(array, middle+1, right)
        merge_indexes(array, left, middle, right)
        return array
    if left >= right:
        return array


if __name__ == '__main__':
    data = read_from_file('../txtf/input.txt')

    n, array = data[0], data[1:]
    result = merge_sort_indexes(array, 0, len(array) - 1)

    write_in_file('../txtf/output.txt', result)

    measuring(merge_sort_indexes, array, 0, len(array) - 1)
