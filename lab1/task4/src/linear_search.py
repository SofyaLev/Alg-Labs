from utils import read, write


def linear_search(A, V):
    result = []
    for i in range(len(A)):
        if A[i] == V:
            result.append(i+1)
    counter = len(result)
    if counter == 0:
        return [-1]
    elif counter == 1:
        return result
    else:
        return counter, result


def main():
    write(end='')
    data = [list(line) for line in read(type_convert=int)]
    array, n = data[0], data[1][0]
    write(*linear_search(array, n), to_end=True)


if __name__ == '__main__':
    main()
