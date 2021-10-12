def merge_arr(arr_1, arr_2, len_1, len_2):
    result = [None] * (len_1 + len_2)
    res_idx = 0
    fst_idx, snd_idx = 0, 0
    while fst_idx <= len_1 and snd_idx <= len_2:
        if arr_1[fst_idx] < arr_2[snd_idx]:
            result[res_idx] = arr_1[fst_idx]
            fst_idx += 1
        else:
            result[res_idx] = arr_2[snd_idx]
            snd_idx += 1
        res_idx += 1
    if fst_idx < len_1:
        result[res_idx:] = arr_1[fst_idx:]
    if snd_idx < len_2:
        result[res_idx:] = arr_2[snd_idx:]
    return result


def find_median(arr_1, arr_2, len_1, len_2):
    full_arr = merge_arr(arr_1, arr_2, len_1, len_2)
    full_len = len_1 + len_2
    mid = full_len // 2
    if full_len % 2 == 1:
        median = full_arr[mid]
    else:
        median = (full_arr[mid] + full_arr[mid + 1]) / 2
    return median


def main():
    north_len = int(input())
    south_len = int(input())
    north = list(map(int, input().split()))
    south = list(map(int, input().split()))
    res = find_median(north, south, north_len, south_len)
    print(res)


if __name__ == '__main__':
    main()
