from utils import read, write


def selection_sort(n, numbers):
    for i in range(n):
        minimum = numbers[i]
        index = i
        for j in range(i+1, n):
            if numbers[j] <= minimum:
                minimum = min(minimum, numbers[j])
                index = j
        numbers.pop(index)
        numbers.insert(i, minimum)

    return numbers


def main():
    write(end='')
    (n,), array = read(type_convert=int)
    write(*selection_sort(n, array), to_end=True)


if __name__ == '__main__':
    main()
