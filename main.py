def sum_negatives_between_min_max(A):
    if not A:
        return 0

    # Находим индексы минимального и максимального элементов
    min_index = A.index(min(A))
    max_index = A.index(max(A))

    # Определяем границы диапазона
    start = min(min_index, max_index) + 1
    end = max(min_index, max_index)

    # Суммируем отрицательные числа в диапазоне [start, end)
    total = sum(x for x in A[start:end] if x < 0)

    return total


# Пример использования
A = [-10, -5, -2, 7, -1, 15]
result = sum_negatives_between_min_max(A)
print("Сумма отрицательных элементов:", result)
