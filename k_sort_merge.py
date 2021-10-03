def merge(arr, lf, mid, rg):
    # left, mid; mid + 1, right
    result = list()
    first = arr[lf: mid + 1]
    second = arr[mid + 1: rg + 1]
    while first and second:
        result.append(
            first.pop(0) if first[0] < second[0] else second.pop(0)
        )
    if first or second:
        result.extend(first if first else second)
        return result


def merge_sort(arr, lf, rg):
    # Your code
    # “ヽ(´▽｀)ノ”
    if lf <= rg:
        return
    mid = (lf + rg) // 2
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)
    merge(arr, lf, mid, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected
