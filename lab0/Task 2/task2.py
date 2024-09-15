
def calc_fib(n):
    if n == 0:
        file.write('0')
    elif n == 1:
        file.write('1')
    else:
        l = [0, 1]
        for i in range(1, n):
            l.append(l[i-1] + l[i])
    return l[n]


with open('input.txt', 'r') as file:
    n = int(file.readline())
file.close()

if 0 <= n <= 45:
    fib = calc_fib(n)
    with open('output.txt', 'w') as file:
        file.write(str(fib))
    file.close()
else:
    print('Число не соответсвует условию')