# Задача 8: K ближайших точек к началу координат

## Описание

В данной задаче реализован алгоритм нахождения K ближайшиз точек к началу координат.

## Структура проекта
```
task8/
├── src/
│   └── closest_points.py
├── tests/
│   └── test_closest_points.py
├── txtf/
│   ├── input.txt
│   └── ounput.txt
└── README.md
```

### Описание файлов
- src/closest_points.py: Реализация алгоритма поиска K лижайших точек к началу координат.


- tests/test_closest_points.py: Файл с тестами работы соответствующей функции.


- txtf/input.txt: Файл, содержащий входные данные.
- txtf/output.txt: Файл для записи выходных данных.

## Как запустить проект

### Установка зависимостей

Проект не требует дополнительных зависимостей, кроме стандартной библиотеки Python. Однако для оценки использования памяти используется модуль psutil, который необходимо установить:
`pip install psutil`

### Запуск алгоритма 

1. Перейдите в директорию с текстовыми файлами задания `txtf/`.
2. Убедитесь, что файл `input.txt` содержит корректные входные данные, соответствующие ограничениям, в следующем формате:
   - Первая строка: число n количество элементов массива и число k - количество искомых точек.
   - Следующие n строк: координаты точек.
3. Перейдите в директорию с основными файлами задания `src/`.
4. Запустите скрипт задания (например, с помощью команды `python closest_points.py`).
5. Результат работы будет записан в файл `output.txt`.

### Запуск тестов

1. Перейдите в директорию с тестами `tests/`.
2. Откройте необходимый файл. 
3. Запустите скрипт теста (например, с помощью команды `python -m unittest test_closest_points.py`).

## Формат входных и выходных данных

### Входной файл (input.txt)
```
n k
x1 y1
...
xn yn
```
- Первая строка: число n количество элементов массива и число k - количество искомых точек.
- Следующие n строк: координаты точек.

### Выходной файл (output.txt)

```
[[x1, y1], ..., [xk, yk]]
```
- Список из k координат ближайших к началу координат точек.

## Описание алгоритма

Алгоритм состоит из следующих шагов:
1. Создание списка расстояний от точек до начала координат:
      - Создается пустой список points
      - Для каждой координаты [x, y] в массиве array вычисляется расстояние от точки до начала координат.
      - Каждая точка добавляется в список points вместе с её расстоянием в виде пары [distance, [x, y]].
2. Список points сортируется по возрастанию расстояния с помощью функции quick_sort.
3. Из первых k элементов отсортированного списка извлекаются сами координаты точек и возвращаются в виде списка.

## Тестирование

В файле с тестами в директории `tests/` реализованы тесты соответствующей функции на разных типах данных: примерах из текста задачи и других значениях.
В основном файле  директории `src/` реализовано тестирование затраченного на выполнение программы времени и памяти.

## Примеры

Входной файл (`input.txt`):
```
2 1
1 3
-2 2
```
Выходной файл (`output.txt`):

```
[[-2, 2]]
```

## Заключение

В ходе решения данной задачи был реализован алгоритм поиска k ближайших к началу координат точек. Также было проведено тестирование алгоритма на корректность его работы и то, сколько памяти и времени затрачивается на его выполнение. 