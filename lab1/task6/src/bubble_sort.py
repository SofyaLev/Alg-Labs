from utils import read, write


def bubble_sort(n, numbers):
    for i in range(n):
        for j in range(i+1, n):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


def main():
    write(end='')
    (n, ), array = read(type_convert=int)
    write(*bubble_sort(n, array), to_end=True)


if __name__ == '__main__':
    main()
