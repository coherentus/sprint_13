"""Ваша задача — по заданной стоимости велосипеда определить

первый день, в которой Вася смог бы купить один велосипед,
и первый день, в который Вася смог бы купить два велосипеда.
Подсказка: решение должно работать за O(log n).

Формат ввода
В первой строке дано число дней n, по которым велись наблюдения за Васиными накоплениями. 1 ≤ n ≤ 106.

В следующей строке записаны n целых неотрицательных чисел. Числа идут в порядке неубывания. Каждое из чисел не превосходит 106.

В третьей строке записано целое положительное число s — стоимость велосипеда. Это число не превосходит 106.

Формат вывода
Нужно вывести два числа — номера дней по условию задачи.

Если необходимой суммы в копилке не нашлось, нужно вернуть -1 вместо номера дня.

"""
from typing import List

def binary_search(arr: List[int], x: int, left: int, right: int) -> int:
    if right <= left: # промежуток пуст
        return left
    # промежуток не пуст
    mid = (left + right) // 2
    if arr[mid] == x: # центральный элемент — искомый
        return mid
    elif x < arr[mid]: # искомый элемент меньше центрального
                       # значит следует искать в левой половине
        return binary_search(arr, x, left, mid)
    else: # иначе следует искать в правой половине
        return binary_search(arr, x, mid + 1, right)

def find_first_day(arr, val) -> int:
    if val > arr[-1]:
        return -1
    return binary_search(arr, val, 0, len(arr)) + 1


def main():
    count_days = int(input())
    days = list(map(int, input().split()))
    cost = int(input())
    answer_1 = find_first_day(days, cost)
    answer_2 = find_first_day(days, cost * 2)
    print(answer_1, answer_2)

if __name__ == '__main__':
    main()
