from utils import read, write


def inversions_merge(array, temp_array, left, middle, right):
    i = left
    j = middle + 1
    k = left
    inversions_counter = 0
    while i <= middle and j <= right:
        if array[i] <= array[j]:
            temp_array[k] = array[i]
            i += 1
        else:
            temp_array[k] = array[j]
            inversions_counter += (middle - i + 1)
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
    return inversions_counter


def inversions_count(array, temp_array, left, right):
    counter = 0
    if left < right:
        middle = (left + right) // 2
        counter += inversions_count(array, temp_array, left, middle)
        counter += inversions_count(array, temp_array, middle+1, right)
        counter += inversions_merge(array, temp_array, left, middle, right)
    return counter


def main():
    write(end='')
    (n, ), array = read(type_convert=int)
    temp_array = [0] * n
    result = inversions_count(array, temp_array, 0, n - 1)
    write(result, to_end=True)


if __name__ == '__main__':
    main()
