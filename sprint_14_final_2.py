# https://contest.yandex.ru/contest/24735/run-report/53610135/
def compare_players(reference, testing):
    """Сравнение итогов двух участников.

    Args:
        reference (list[str, int, int]): Имя, баллы, штраф.
        testing (list[str, int, int]): Имя, баллы, штраф.
    Returns:
        (str): 'left' - проверяемый должен стать левее(выше местом).
               'right' - должен стать правее(ниже местом).
               'identical' - объекты идентичны, двигать не надо.
    Правила сортировки - баллы по убыванию, штраф по возрастанию,
    имя по алфавиту.
    """
    if reference == testing:
        return 'identical'
    # очки за задачи
    if reference[1] > testing[1]:
        return 'right'
    if reference[1] < testing[1]:
        return 'left'
    # очки равны, сравнить штраф
    if reference[2] < testing[2]:
        return 'right'
    if reference[2] > testing[2]:
        return 'left'
    # штрафы равны, сравнить ники
    return 'left' if testing[0] < reference[0] else 'right'


def get_pivot(arr, left, right):
    """Выбор медианного значения для быстрой сортировки.

    Args:
        arr (list[[str, int, int],...]): Имя, баллы, штраф.
        Функция оперирует значениями из arr[left: right + 1]
    Return:
        (int): индекс 'медианного' эл-та.
    Для начального, серединного и конечного эл-тов диапазона взять
    индекс и значение поля 'баллы' и в виде кортежей записать в median.
    Отсортировать median по возрастанию баллов.
    Из median[1] вернуть индекс эл-та.
    """
    mid = (left + right) // 2
    median = [None] * 3
    median[0] = (left, arr[left][1])
    median[1] = (mid, arr[mid][1])
    median[2] = (right, arr[right][1])
    for i in range(2):
        if median[i][1] > median[i + 1][1]:
            median[i + 1], median[i] = median[i], median[i + 1]
    if median[0][1] > median[1][1]:
        median[0], median[1] = median[1], median[0]
    return median[1][0]


def qsort(arr, left, right):
    """Сортировка массива по трём составлющим 'на месте'.

    Args:
        arr (list[[str, int, int],...]): Имя, баллы, штраф.
        left (int): левый индекс диапазона
        right (int): правый индекс диапазона
    """
    if right - left <= 0:
        return
    i, j = left, right

    pivot = get_pivot(arr, left, right)
    reference = arr[pivot]
    while i <= j:
        while compare_players(reference, arr[i]) == 'left':
            i += 1
        while compare_players(reference, arr[j]) == 'right':
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i, j = i + 1, j - 1

    qsort(arr, left, j)
    qsort(arr, i, right)


def get_order(players):
    """Запуск сортировки и возврат требуемых значений.

    Args:
        players (list[[str, int, int],...]) - Имя, баллы, штраф.
    Returns:
        result (list[str]) - Имя.
    """
    qsort(players, 0, len(players) - 1)
    return [row[0] for row in players]


def main():
    count_item = int(input())
    items = [None] * count_item
    for i in range(count_item):
        name, points, penalty = input().split()
        items[i] = [name, int(points), int(penalty)]

    result = get_order(items)
    print('\n'.join(result))


if __name__ == '__main__':
    main()
