a = [5, 2, 4, 6, 1, 3, 2, 6]

def merge_sort(a):
    # Реализация сортировки слиянием
    if len(a) < 2:
        return a[:]  # Базовый случай: если массив содержит 1 элемент или меньше, возвращаем его без изменений
    else:
        median = int(len(a) / 2)  # Находим середину массива
        left = merge_sort(a[:median])  # Рекурсивно сортируем левую половину
        right = merge_sort(a[median:])  # Рекурсивно сортируем правую половину
        return merge(left, right)  # Вызываем функцию слияния для отсортированных половин

def merge(left, right):
    # Функция слияния двух отсортированных массивов
    res = []  # Результирующий массив
    i, j = 0, 0  # Индексы для обхода левого и правого массивов соответственно
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])  # Если элемент в левом массиве меньше, добавляем его в результирующий массив
            i += 1
        else:
            res.append(right[j])  # Иначе добавляем элемент из правого массива в результирующий массив
            j += 1
    while i < len(left):
        res.append(left[i])  # Добавляем оставшиеся элементы из левого массива в результирующий массив
        i += 1
    while j < len(right):
        res.append(right[j])  # Добавляем оставшиеся элементы из правого массива в результирующий массив
        j += 1
    return res  # Возвращаем отсортированный массив

print(merge_sort(a))  # Выводим результат сортировки