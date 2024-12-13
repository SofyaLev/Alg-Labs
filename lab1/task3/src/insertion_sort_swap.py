from utils import read, write


def swap(a, b):
    a, b = b, a
    return a, b


def insertion_sort_swap(n, numbers):
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = swap(numbers[i], numbers[j])
                i, j = j, i
    return numbers


def main():
    write(end='')
    (n,), array = read(type_convert=int)
    write(*insertion_sort_swap(n, array), to_end=True)


if __name__ == '__main__':
    main()
