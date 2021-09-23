def broken_search(nums, target) -> int:
    #  Your code
    #  “ヽ(´▽｀)ノ”
    
    def bin_search(arr, x, left, right):
        arr_len = len(arr)
        if arr_len < 4:
            for i in range(arr_len):
                if arr[i][1] == x:
                    return arr[i][0]
            return -1

        # center
        mid = (left + right) // 2
        # sorted half ?
        if arr[mid][1] >= arr[left][1]: # sorted            
            # check x in sorted
            if arr[left][1] <= x <= arr[mid][1]:
                if arr[mid][1] == x:
                    return arr[mid][0]
                if arr[left][1] == x:
                    return arr[left][0]
                return binary_search(arr, x, left + 1, mid)
            unsorted = arr[mid + 1: right + 1]
        else:
            # sorted from mid to right
            # check x in sorted
            if arr[mid][1] <= x <= arr[right][1]:
                if arr[mid][1] == x:
                    return arr[mid][0]
                if arr[right][1] == x:
                    return arr[right][0]
                return binary_search(arr, x, mid + 1, right)
            unsorted = arr[left: mid]
        
        return bin_search(unsorted, x, 0, len(unsorted))
    

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

    inspected = list(enumerate(nums))
    
    bin_search(inspected, target, 0, len(inspected))

def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
