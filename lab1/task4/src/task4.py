def linear_search(A, V):
    result = []
    for i in range(len(A)):
        if A[i] == V:
            result.append(i+1)
    counter = len(result)
    if counter == 0:
        return -1
    elif counter == 1:
        return result
    else:
        return counter, result


# with open('input.txt', 'r') as file:
#     A = list(map(int, file.readline().split()))
#     V = int(file.readline())
# file.close()
#
# if (0 <= len(A) <= 10**3) and (-10**3 <= V <= 10**3):
#     with open('output.txt', 'w') as file:
#         file.write(', '.join(map(str, linear_search(A, V))))
#     file.close()
# else:
#     print('Введенные данные не соответствуют условию')