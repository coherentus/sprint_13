# https://contest.yandex.ru/contest/24735/run-report/53706565/
def broken_search(nums, target) -> int:
    """Бинарный поиск в 'сломанном' списке.

    Args:
        nums (List): массив, бывший отсортированным в кольцевой структуре
        target ([type]): искомый эл-т
    Returns:
        int: индекс искомого эл-та, или -1 если не найден
    Алгоритм поиска:
    Массив делится на две части посередине.
    Одна точно должна быть упорядоченна. Могут быть обе, если деление
    попало на 'ступеньку'.
    Если часть отсортирована, легко проверяется, входит ли в неё X.
    Итого:
    За left, right берутся индексы первого и последнего эл-тов.
    В цикле пока диапазон не схлопнется:
    Делим на части
    Проверяем mid == X
    Если левая сортирована:
        если X входит:
            индексы левой для след. итерации
        иначе:
            индексы правой для след. итерации
    иначе:
        если X входит:
            индексы правой для след. итерации
        иначе:
            индексы левой для след. итерации
    след. итерация
    """
    left, right = 0, len(nums) - 1

    while True:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if left == right:
            return -1

        # левая часть
        if nums[left] < nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid
            else:
                left = mid + 1
        else:  # правая часть
            if nums[mid + 1] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid
