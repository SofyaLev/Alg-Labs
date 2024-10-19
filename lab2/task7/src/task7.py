from lab2.task7.src.find_max_subarray import find_max_subarray

with open('input.txt', 'r') as file:
    n = int(file.readline())
    numbers = list(map(int, file.readline().split()))
file.close()

if 1 <= n <= 10**5:
    with open('output.txt', 'w') as file:
        max_sum, left, right = find_max_subarray(n, numbers)
        file.write(f'Максимальная сумма: {max_sum}, начальный индекс: {left}, конечный индекс: {right}')
    file.close()
else:
    print('Введенные данные не соответствуют условию')
