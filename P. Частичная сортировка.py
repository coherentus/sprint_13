def find_segments(arr, len_arr) -> int:
    """Найти и вернуть кол-во сегментов."""
    count = 0
    summ_val = 0
    summ_idx = 0
    for i in range(len_arr):
        summ_val += arr[i]
        summ_idx += i
        if summ_val == summ_idx:
            count += 1
            summ_val = 0
            summ_idx = 0
    return count


def main():
    count_nums = int(input())
    nums = list(map(int, input().split()))
    res = find_segments(nums, count_nums)
    print(res)


if __name__ == '__main__':
    main()
