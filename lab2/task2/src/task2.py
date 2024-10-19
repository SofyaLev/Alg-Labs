from lab2.task2.src.merge_sort_indexes import merge_sort_indexes

with open('input.txt', 'r') as file:
    n = int(file.readline())
    numbers = list(map(int, file.readline().split()))
file.close()

if 1 <= n <= 10**5:
    with open('output.txt', 'w') as file:
        file.write(' '.join(map(str, merge_sort_indexes(numbers, 0, len(numbers)-1))))
    file.close()
else:
    print('Введенные данные не соответствуют условию')
