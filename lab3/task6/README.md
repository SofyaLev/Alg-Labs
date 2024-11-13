# Задача 6: Сортировка целых чисел

## Описание

В данной задаче реализован алгоритм сортировки массива чисел вида A[i] * B[j], где 1 <= i <= n и ш <= j <= m и вывести сумму каждого десятого элемента полученной последовательности.

## Структура проекта
```
task6/
├── src/
│   └── sum_of_tenths.py
├── tests/
│   └── test_sum_of_tenths.py
├── txtf/
│   ├── input.txt
│   └── ounput.txt
└── README.md
```

### Описание файлов
- src/sum_of_tenths.py: Реализация алгоритма перемножения элементов двух данных массивов, сортировки полученных чисел и вывода суммы каждого десятого из них.


- tests/test_sum_of_tenths.py: Файл с тестами работы соответствующей функции.


- txtf/input.txt: Файл, содержащий входные данные.
- txtf/output.txt: Файл для записи выходных данных.

## Как запустить проект

### Установка зависимостей

Проект не требует дополнительных зависимостей, кроме стандартной библиотеки Python. Однако для оценки использования памяти используется модуль psutil, который необходимо установить:
`pip install psutil`

### Запуск алгоритма 

1. Перейдите в директорию с текстовыми файлами задания `txtf/`.
2. Убедитесь, что файл `input.txt` содержит корректные входные данные, соответствующие ограничениям, в следующем формате:
   - Первая строка: числа n и m - количество элементов массивов A и B соответственно.
   - Вторая строка: n целых чисел, разделённых пробелами.
   - Третья строка: m целых чисел, разделённых пробелами.
3. Перейдите в директорию с основными файлами задания `src/`.
4. Запустите скрипт задания (например, с помощью команды `python sum_of_tenths.py`).
5. Результат работы будет записан в файл `output.txt`.

### Запуск тестов

1. Перейдите в директорию с тестами `tests/`.
2. Откройте необходимый файл. 
3. Запустите скрипт теста (например, с помощью команды `python -m unittest test_sum_of_tenths.py`).

## Формат входных и выходных данных

### Входной файл (input.txt)
```
n m
a1 a2 a3 ... an
b1 b2 b3 ... bm
```
- Первая строка: числа n и m - количество элементов массивов A и B соответственно.
- Вторая строка: n целых чисел, разделённых пробелами.
- Третья строка: m целых чисел, разделённых пробелами.

### Выходной файл (output.txt)

```
result
```
- Сумма каждого десятого числа полученной в результате сортировки последовательности.

## Описание алгоритма

Алгоритм состоит из следующих шагов:
1. Сначала формируется новый список, содержащий произведения всех возможных комбинаций элементов двух исходных списков.
2. Этот список сортируется методом быстрой сортировки.
3. Из отсортированного списка берутся каждые десятые значения и суммируются.
4. Сумма этих значений возвращается как итоговый результат.

## Тестирование

В файле с тестами в директории `tests/` реализованы тесты соответствующей функции на разных типах данных: примере из текста задачи, отсортированных в разном порядке массивах и пустых массивах.
В основном файле  директории `src/` реализовано тестирование затраченного на выполнение программы времени и памяти.

## Примеры

Входной файл (`input.txt`):
```
4 4
7 1 4 9
2 7 8 11
```
Выходной файл (`output.txt`):

```
51
```

## Заключение

В ходе решения данной задачи был реализован алгоритм перемножения элементов двух данных массивов, сортировки полученных чисел и вывода суммы каждого десятого из них. Также было проведено тестирование алгоритма на корректность его работы и то, сколько памяти и времени затрачивается на его выполнение. 