from utils import read, write


def insertion_sort_plus(n, numbers):
    indexes = [1]
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                i, j = j, i
        indexes.append(i+1)
    return indexes, numbers


def main():
    write(end='')
    (n, ), array = read(type_convert=int)
    result = insertion_sort_plus(n, array)
    for line in result:
        write(*line, to_end=True)


if __name__ == '__main__':
    main()
