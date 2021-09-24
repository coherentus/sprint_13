def broken_search(nums, target) -> int:
    #  Your code
    #  “ヽ(´▽｀)ノ”
    
    def binary_search(arr, x, left, right) -> int:
        if right <= left: # промежуток пуст
            return -1
        # промежуток не пуст
        mid = (left + right) // 2
        if arr[mid] == x: # центральный элемент — искомый
            return arr[mid]
        elif x < arr[mid]: # искомый элемент меньше центрального
                        # значит следует искать в левой половине
            return binary_search(arr, x, left, mid)
        else: # иначе следует искать в правой половине
            return binary_search(arr, x, mid + 1, right)

    def bin_brk_search(arr, x, left, right):
        arr_len = len(arr)
        if arr_len < 4:
            for i in range(arr_len):
                if arr[i] == x:
                    return arr[i]
            return -1

        # center
        mid = (left + right) // 2

        if arr[mid] > arr[left]:
            sorted_half = (left, mid)
            unsorted_half = (mid + 1, right)
        else:
            unsorted_half = (left, mid - 1)
            sorted_half = (mid, right)
        if arr[sorted_half[0]] <= x <= arr[sorted_half[1]]:
            return binary_search(arr, x, sorted_half[0], sorted_half[1])
        else:
            return bin_brk_search(arr, x, unsorted_half[0], unsorted_half[1])
        
    
    inspected = nums
    
    return bin_brk_search(inspected, target, 0, len(inspected) - 1)

def main():
    count_item = int(input())
    find_x = int(input())
    items = list(map(int, input().split()))
    
    result = broken_search(items, find_x)
    print(result)


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6

if __name__ == '__main__':
    main()



"""
9
5
19 21 100 101 1 4 5 7 12

2
1
5 1

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