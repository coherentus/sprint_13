def sort_arr(arr):
    """Cортировать слиянием."""
    if len(arr) == 1:
        return arr
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        # разделение на две части
        lf_segment = sort_arr(arr[left: mid + 1])
        rg_segment = sort_arr(arr[mid + 1: right + 1])

        # объединение частей
        lf_len = len(lf_segment)
        rg_len = len(rg_segment)
        res = [None] * (lf_len + rg_len)
        lf_idx, rg_idx = 0, 0
        res_idx = 0
        while (lf_idx < lf_len) and (rg_idx < rg_len):
            lf_val = lf_segment[lf_idx]
            rg_val = rg_segment[rg_idx]
            if int(lf_val + rg_val) > int(rg_val + lf_val):
                res[res_idx] = lf_val
                lf_idx += 1
            else:
                res[res_idx] = rg_val
                rg_idx += 1
            res_idx += 1
        if lf_idx < lf_len:
            res[res_idx:] = lf_segment[lf_idx:]
        if rg_idx < rg_len:
            res[res_idx:] = rg_segment[rg_idx:]
        return res


def max_glue_num(arr, lenght):
    """Отсортировать, склеить и отдать."""
    left, right = 0, lenght - 1
    result = sort_arr(arr)
    return ''.join(result)


def main():
    count_nums = int(input())
    nums = input().split()
    print(max_glue_num(nums, count_nums))


if __name__ == '__main__':
    main()
