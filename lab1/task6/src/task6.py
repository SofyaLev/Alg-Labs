def bubble_sort(n, numbers):
    for i in range(n):
        for j in range(i+1, n):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


def check(numbers):
    for i in range(len(numbers)-1):
        if not(numbers[i] <= numbers[i+1]):
            return False
    return True


with open('input.txt', 'r') as file:
    n = int(file.readline())
    numbers = list(map(int, file.readline().split()))
file.close()

if 1 <= n <= 10**3:
    with open('output.txt', 'w') as file:
        file.write(' '.join(map(str, bubble_sort(n, numbers))))
    file.close()
else:
    print('веденные данные не соответствуют условию')

print(check(bubble_sort(n, numbers)))