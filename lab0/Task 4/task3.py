import time
start = time.perf_counter()
with open('input.txt', 'r') as file:
    n = int(file.readline())

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
print(time.perf_counter() - start)
