def insertion_sort(n, numbers):
    indexes = [1]
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                i, j = j, i
        indexes.append(i+1)
    return numbers, indexes


# with open('input.txt', 'r') as file:
#     n = int(file.readline())
#     numbers = list(map(int, file.readline().split()))
# file.close()
#
# result_numbers, result_indexes = insertion_sort(n, numbers)
#
# if 1 <= n <= 10**3:
#     with open('output.txt', 'w') as file:
#         file.write(' '.join(map(str, result_indexes)))
#         file.write('\n')
#         file.write(' '.join(map(str, result_numbers)))
#     file.close()
# else:
#     print('Введенные данные не соответствуют условию')
