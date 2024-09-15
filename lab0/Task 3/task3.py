with open('input.txt', 'r') as file:
    n = int(file.readline())

if 0 <= n <= 10**7:
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        a, b = 0, 1
        for _ in range(n-1):
            a, b = b, a + b

    with open('output.txt', 'w') as file:
        file.write(str(b % 10))
    file.close()
else:
    print('Число не соответствует условию')
