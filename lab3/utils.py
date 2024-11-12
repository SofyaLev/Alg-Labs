import random
import time
import psutil


def read_from_file(filename: str, type = int):
    f = open(filename, "r")
    if type == str:
        data = f.read()
        return data
    data = list(map(int, f.read().split()))
    return data


def write_in_file(filename: str, array: any, split_str: str = ' ') -> None:
    with open(filename, 'w') as f:
        f.write(split_str.join(map(str, array)))
    return None


def print_time_memory(time, memory):
    print(f'Время: {time} секунд')
    print(f'Память: {memory} МБ')


def generate_random_array(n, left, right):
    array = [random.randint(left, right+1) for _ in range(1, n+1)]
    return array


def measuring(task_func, *args):

    start_time = time.perf_counter()
    result = task_func(*args)
    end_time = time.perf_counter() - start_time

    memory = psutil.Process().memory_info().rss / 1024 ** 2

    print(f"Время: {end_time * 1e2} секунд")
    print(f"Память: {memory} Мб")