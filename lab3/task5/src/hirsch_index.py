from lab3.utils import read_from_file, write_in_file, measuring
from lab3.task1.src.quick_sort import quick_sort


def hirsch_index(citations):
    n = len(citations)
    quick_sort(citations, 0, n-1)
    for h in range(n):
        if (n - h) <= citations[h]:
            return n - h
    return 0


if __name__ == '__main__':
    data = read_from_file('../txtf/input.txt')

    result = hirsch_index(data)

    write_in_file('../txtf/output.txt', [result])

    measuring(hirsch_index, data)
