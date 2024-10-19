from lab2.task5.src.majority_element import majority_element

with open('input.txt', 'r') as file:
    n = int(file.readline())
    numbers = list(map(int, file.readline().split()))
file.close()

if 1 <= n <= 10**5:
    with open('output.txt', 'w') as file:
        file.write(str(majority_element(numbers)))
    file.close()
else:
    print('Введенные данные не соответствуют условию')
