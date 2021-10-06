def sort_arr(arr, lf, rg):
    if rg - lf <= 1:
        return
    mid = (lf + rg) // 2
    sort_arr(arr, lf, mid)
    sort_arr(arr, mid + 1, rg)
    arr[lf: rg] = merge(arr, lf, mid, rg)


def merge(arr, lf, mid, rg):
    # left, mid; mid + 1, right
    first = arr[lf: mid]
    second = arr[mid: rg]
    if not first:
        return second
    if not second:
        return first
    l_first = len(first)
    l_second = len(second)
    f_idx = 0
    s_idx = 0
    result = [None] * (l_first + l_second)
    res_idx = 0
    while True:
        first_elem = first[f_idx]
        second_elem = second[s_idx]
        if int(first_elem + second_elem) > int(second_elem + first_elem):
            result[res_idx] = first_elem
            f_idx += 1
            res_idx += 1
        else:
            result[res_idx] = second_elem
            s_idx += 1
            res_idx += 1
        if f_idx == l_first:
            ended = 1
            break
        if s_idx == l_second:
            ended = 2
            break
    if ended == 2:
        result[res_idx:] = first[f_idx:]
    else:
        result[res_idx:] = second[s_idx:]
    return result


def max_glue_num(arr, lenght):
    """Отсортировать, склеить и отдать."""
    left, right = 0, len(arr) - 1
    sort_arr(arr, left, right)

    res = ''
    for item in arr:
        res = res + item
    return res


def main():
    count_nums = int(input())
    nums = input().split()
    print(max_glue_num(nums, count_nums))


if __name__ == '__main__':
    main()
