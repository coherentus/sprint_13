# https://contest.yandex.ru/contest/24735/run-report/53678398/
def compare_players(reference, testing):
    """Сравнение итогов двух участников.

    Args:
        reference (list[int, int, str]): Баллы, штраф, имя.
        testing (list[int, int, str]): Баллы, штраф, имя.
    Returns:
        (str): 'left' - проверяемый должен стать левее(выше местом).
               'right' - должен стать правее(ниже местом).
               'identical' - объекты идентичны, двигать не надо.
    Правила сортировки - баллы по убыванию, штраф по возрастанию,
    имя по алфавиту. Исходный массив при считывании уже подготовлен.
    """
    if reference == testing:
        return 'identical'
    return 'left' if reference > testing else 'right'


def qsort(arr, left, right):
    """Сортировка массива по трём составлющим 'на месте'.

    Args:
        arr (list[[int, int, str],...]): Баллы, штраф, имя.
        left (int): левый индекс диапазона
        right (int): правый индекс диапазона
    """
    if right <= left:
        return
    left_idx = left
    right_idx = right

    pivot = (left + right) // 2
    reference = arr[pivot]
    while left_idx <= right_idx:
        while compare_players(reference, arr[left_idx]) == 'left':
            left_idx += 1
        while compare_players(reference, arr[right_idx]) == 'right':
            right_idx -= 1
        if left_idx <= right_idx:
            arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]
            left_idx += 1
            right_idx -= 1

    qsort(arr, left, right_idx)
    qsort(arr, left_idx, right)


def get_order(players):
    """Запуск сортировки и возврат требуемых значений.

    Args:
        players (list[[int, int, str],...]) - Баллы, штраф, имя.
    Returns:
        result (list[str]) - Имя.
    """
    qsort(players, 0, len(players) - 1)
    return [row[2] for row in players]


def main():
    count_line = int(input())
    persons = [None] * count_line
    for i in range(count_line):
        name, points, penalty = input().split()
        # формирование массива для удобства сравнения
        persons[i] = [-int(points), int(penalty), name]

    result = get_order(persons)
    print('\n'.join(result))


if __name__ == '__main__':
    main()
