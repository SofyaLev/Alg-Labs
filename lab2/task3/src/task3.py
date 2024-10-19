from lab2.task3.src.inversions_count import inversions_merge_sort

with open('input.txt', 'r') as file:
    n = int(file.readline())
    numbers = list(map(int, file.readline().split()))
file.close()

if 1 <= n <= 10**5:
    with open('output.txt', 'w') as file:
        file.write(str(inversions_merge_sort(numbers, [0]*len(numbers), 0, len(numbers)-1)))
    file.close()
else:
    print('Введенные данные не соответствуют условию')
