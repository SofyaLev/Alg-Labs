from utils import read, write


def swap(a, b):
    c = b
    b = a
    a = c
    return a, b


def rec_insertion_sort_swap(n, numbers, i=1):
    if i != n:
        for j in range(i-1, -1, -1):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = swap(numbers[i], numbers[j])
                i, j = j, i
        return rec_insertion_sort_swap(n, numbers, i+1)
    else:
        return numbers


def main():
    write(end='')
    (n,), array = read(type_convert=int)
    write(*rec_insertion_sort_swap(n, array), to_end=True)


if __name__ == '__main__':
    main()
