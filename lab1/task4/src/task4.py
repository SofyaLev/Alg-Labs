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


# A = list(map(int, input().split()))
# V = int(input())
#
# if (0 <= len(A) <= 10**3) and (-10**3 <= V <= 10**3):
#     print(*linear_search(A, V), sep=', ')
# else:
#     print('Введенные данные не соответсвуют условию')
