from lab2.task4.src.binary_search import search_elements

with open('input.txt', 'r') as file:
    n = int(file.readline())
    a = list(map(int, file.readline().split()))
    k = int(file.readline())
    b = list(map(int, file.readline().split()))
file.close()

if 1 <= n <= 10**5 and 1 <= k <= 10**5:
    with open('output.txt', 'w') as file:
        result = search_elements(a, b)
        file.write(', '.join(map(str, result)))
    file.close()
else:
    print('Введенные данные не соответствуют условию')
