def swap(a, b):
    c = b
    b = a
    a = c
    return a, b


def insertion_sort_swap(n, numbers):
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = swap(numbers[i], numbers[j])
                i, j = j, i
    return numbers


# with open('input.txt', 'r') as file:
#     n = int(file.readline())
#     numbers = list(map(int, file.readline().split()))
# file.close()
#
# if 1 <= n <= 10**3:
#     with open('output.txt', 'w') as file:
#         file.write(' '.join(map(str, insertion_sort_swap(n, numbers))))
#     file.close()
# else:
#     print('Введенные данные не соответствуют условию')
