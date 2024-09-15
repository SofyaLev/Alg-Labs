with open('input.txt', 'r') as file:
    a, b = map(int, file.readline().split())
file.close()

if -10**9 <= a <= 10**9 and -10**9 <= b <= 10**9:
    with open('output.txt', 'w') as file:
        file.write(str(a + b))
    file.close()
else:
    print('Числа не соответствуют условию')