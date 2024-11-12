from lab3.utils import read_from_file, write_in_file, measuring


def scarecrow_sort(n, k, array):
    for i in range(0, n-k):
        if array[i] > array[i+k]:
            array[i], array[i+k] = array[i+k], array[i]
    return "YES" if array == sorted(array) else "NO"


if __name__ == '__main__':
    data = read_from_file('../txtf/input.txt')

    n, k = data[:2]
    array = data[2:]
    result = scarecrow_sort(n, k, array)

    write_in_file('../txtf/output.txt', [result])

    measuring(scarecrow_sort, n, k, array)
