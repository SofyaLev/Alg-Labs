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


# with open('input.txt', 'r') as file:
#     n = int(file.readline())
#     numbers = list(map(int, file.readline().split()))
# file.close()
#
# if 1 <= n <= 10**3:
#     with open('output.txt', 'w') as file:
#         file.write(' '.join(map(str, selection_sort(n, numbers))))
#     file.close()
# else:
#     print('Введенные данные не соответствуют условию')
