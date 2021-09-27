def broken_search(nums, target) -> int:
    from typing import List
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
        Проверить сортированность частей. Возможны три варианта:
        1. левая - да; правая - нет
        2. левая - нет; правая - да
        3. левая - да; правая - да
        Для случаев 1 и 2, если сортированная часть содержит X, передать её
        в простой бинарный поиск bin_search(), если нет, передать другую,
        несортированную часть, в bin_brk_search().
        Для варианта три передать в простой bin_search() ту часть, которая
        содержит X.
    """        
    def binary_search(arr, x, left, right) -> int:
        if right <= left: # дошли до края
            if x == arr[left]:
                return left
            return -1
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return binary_search(arr, x, left, mid)
        else:
            return binary_search(arr, x, mid + 1, right)

    def bin_brk_search(arr, x, left, right):
        if right - left < 4: # дошли до края
            for i in range(left, right + 1):
                if x == arr[i]:
                    return i
            return -1
        # [сортированность, начало, конец]
        left_payload: List[bool, int, int] = [False, -1, -1]
        right_payload: List[bool, bool, int, int] = [False, -1, -1]
        # середина
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid

        # левая часть
        if arr[left] < arr[mid]:
            left_payload[0] = True
            if arr[left] < x < arr[mid]:
                return binary_search(arr, x, left, mid - 1)
            left_payload[1:] = left, mid - 1

        # правая часть
        if arr[mid] < arr[right]:
            right_payload[0] = True
            if arr[mid] < x < arr[right]:
                return binary_search(arr, x, mid, right)
            right_payload[1:] = mid, right
        
        # в отсортированные части X не входит
        if left_payload[0]:
            left, right = right_payload[1:]
        else:
            left, right = left_payload[1:]

        return bin_brk_search(arr, x, left, right)

    return bin_brk_search(nums, target, 0, len(nums) - 1)

def main():
    count_item = int(input())
    find_x = int(input())
    items = list(map(int, input().split()))
    
    result = broken_search(items, find_x)
    print(result)


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
    arr = [5, 1]
    assert broken_search(arr, 1) == 2
    



if __name__ == '__main__':
    main()



"""
9
5
19 21 100 101 1 4 5 7 12


8
3
1 2 3 5 6 7 9 0

7
5
0 2 6 7 8 9 10

1
1
1

3
8
3 6 7

11
1
1 2 3 4 5 6 7 8 9 10 0

"""