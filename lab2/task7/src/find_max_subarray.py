from lab2.utils import read_from_file, write_in_file, measuring


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
    data = read_from_file('../txtf/input.txt')

    n, array = data[0], data[1:]
    result = find_max_subarray(n, array)

    write_in_file('../txtf/output.txt', result)

    measuring(find_max_subarray, n, array)
