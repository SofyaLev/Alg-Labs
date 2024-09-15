import time
start = time.perf_counter()
def calc_fib(n):
    if n == 0:
        res = '0'
    elif n == 1:
        res = '1'
    else:
        a, b = 0, 1
        for _ in range(n-1):
            a, b = b, (a + b) % 10
        res = b
    return res


with open('input.txt', 'r') as file:
    n = int(file.readline())
file.close()

if 0 <= n <= 10**7:
    fib = calc_fib(n)
    with open('output.txt', 'w') as file:
        file.write(str(fib))
    file.close()
else:
    print('Число не соответствует условию')

print(time.perf_counter() - start)
