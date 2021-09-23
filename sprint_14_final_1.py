def broken_search(nums, target) -> int:
    #  Your code
    #  “ヽ(´▽｀)ノ”
    
    def binary_search(arr, x, right, left) -> int:
        if right <= left: # промежуток пуст
            return -1
        # промежуток не пуст
        mid = (left + right) // 2
        if arr[mid][1] == x: # центральный элемент — искомый
            return arr[mid][0]
        elif x < arr[mid][1]: # искомый элемент меньше центрального
                        # значит следует искать в левой половине
            return binary_search(arr, x, left, mid)
        else: # иначе следует искать в правой половине
            return binary_search(arr, x, mid + 1, right)

    def bin_search(arr, x, left, right):
        arr_len = len(arr)
        if arr_len < 4:
            for i in range(arr_len):
                if arr[i][1] == x:
                    return arr[i][0]
            return -1

        # center
        mid = (left + right) // 2

        if arr[mid][1] > arr[left][1]:
            sorted = (left, mid)
            unsorted = (mid + 1, right)
        else:
            unsorted = (left, mid - 1)
            sorted = (mid, right)
        if arr[sorted[0]] <= x <= arr[sorted[1]]:
            return binary_search(sorted, x, sorted[0], sorted[1])
        else:
            return bin_search(unsorted, x, unsorted[0], unsorted[1])
        
    
    inspected = list(enumerate(nums))
    
    return bin_search(inspected, target, 0, len(inspected))

def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
