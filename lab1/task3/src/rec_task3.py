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


# with open('input.txt', 'r') as file:
#     n = int(file.readline())
#     numbers = list(map(int, file.readline().split()))
# file.close()
#
# if 1 <= n <= 10**3:
#     with open('output.txt', 'w') as file:
#         file.write(' '.join(map(str, rec_insertion_sort_swap(n, numbers))))
#     file.close()
# else:
#     print('Введенные данные не соответствуют условию')
