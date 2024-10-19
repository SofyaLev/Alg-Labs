from lab2.task1.src.merge_sort import merge_sort

with open('input.txt', 'r') as file:
    n = int(file.readline())
    numbers = list(map(int, file.readline().split()))
file.close()

if 1 <= n <= 2 * 10**4:
    with open('output.txt', 'w') as file:
        file.write(' '.join(map(str, merge_sort(numbers, 0, len(numbers)-1))))
    file.close()
else:
    print('Введенные данные не соответствуют условию')
