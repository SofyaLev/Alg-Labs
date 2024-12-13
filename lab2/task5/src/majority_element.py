from utils import read, write


def majority_element(array):
    def find_candidate(array):
        count = 0
        candidate = None
        for number in array:
            if count == 0:
                candidate = number
                count = 1
            elif number == candidate:
                count += 1
            else:
                count -= 1

        return candidate

    def is_majority(array, candidate):
        count = sum(1 for number in array if number == candidate)
        return count > len(array) // 2

    candidate = find_candidate(array)

    if is_majority(array, candidate):
        return 1
    else:
        return 0


def main():
    write(end='')
    (n,), array = read(type_convert=int)
    write(majority_element(array), to_end=True)


if __name__ == '__main__':
    main()
