from utils import read, write


def insertion_sort(n, numbers):
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                i, j = j, i
    return numbers


def main():
    write(end='')
    (n, ), array = read(type_convert=int)
    write(*insertion_sort(n, array), to_end=True)


if __name__ == '__main__':
    main()
