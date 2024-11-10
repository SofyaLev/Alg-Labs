import os
import random


def read_file(task):
    """
    Функция для чтения входных данных из файла 'input.txt'.
    Возвращает список строк без символов перевода строки.
    """
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), f'task{task}', 'txtf', 'input.txt'))
    with open(base_path, 'r') as f:
        return [line.strip() for line in f.readlines()]


def write_output(task, *args):
    """
    Функция для записи выходных данных в файл 'output.txt'.
    Принимает переменное количество аргументов и записывает каждый на новой строке.
    """
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), f'task{task}', 'txtf', 'output.txt'))
    with open(base_path, 'w') as f:
        for arg in args:
            print(arg, file=f)


def generate_random_array(n, left, right):
    """
    :param n: длина массива
    :param left: левая граница элеметов массива
    :param right: правая граница элементов массива
    :return: массив длины n случайных чисел из диапазона от left до right включительно
    """
    array = [random.randint(left, right+1) for _ in range(1, n+1)]
    return array
