from lab2.utils import read_from_file, write_in_file, measuring


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
    data = read_from_file('../txtf/input.txt')

    n, array = data[0], data[1:]
    temp_array = [0] * n
    result = inversions_count(array, temp_array,  0, len(array) - 1)

    write_in_file('../txtf/output.txt', [result])

    measuring(inversions_count, array, temp_array,  0, len(array) - 1)
