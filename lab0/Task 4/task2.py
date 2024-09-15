import time
start = time.perf_counter()

with open('input.txt', 'r') as file:
    n = int(file.readline())
file.close()

with open('output.txt', 'w') as file:
    if n == 0:
        file.write('0')
    elif n == 1:
        file.write('1')
    else:
        l = [0, 1]
        for i in range(1, n):
            l.append(l[i-1] + l[i])
        file.write(str(l[n]))
file.close()
print(time.perf_counter() - start)