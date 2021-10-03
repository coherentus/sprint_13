def merge(arr, lf, mid, rg):
    # left, mid; mid + 1, right
    result = list()
    first = arr[lf: mid]
    second = arr[mid: rg]
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
    if rg - lf <= 1:
        return
    mid = (lf + rg) // 2
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)
    arr = merge(arr, lf, mid, rg)
