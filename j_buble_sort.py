def buble_sort(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]

def check_sort(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return False
    return True


def main():
    count_nums = int(input())
    nums = list(map(int, input().split()))
    if check_sort(nums):
        print(*nums)
    else:
        while not check_sort(nums):
            buble_sort(nums)
            print(*nums)


if __name__ == '__main__':
    main()
