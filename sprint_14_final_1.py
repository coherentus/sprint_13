def broken_search(nums, target) -> int:
    #  Your code
    #  “ヽ(´▽｀)ノ”
    enum_nums = list(enumerate(nums))
    sorted_enum = sorted(enum_nums, key=lambda x: x[1])    

    def binary_search(arr, x, right, left) -> int:
        if right <= left: # промежуток пуст
            return -1
        # промежуток не пуст
        mid = (left + right) // 2
        if arr[mid][1] == x: # центральный элемент — искомый
            return mid
        elif x < arr[mid][1]: # искомый элемент меньше центрального
                        # значит следует искать в левой половине
            return binary_search(arr, x, left, mid)
        else: # иначе следует искать в правой половине
            return binary_search(arr, x, mid + 1, right)
    
    result = binary_search(sorted_enum, target, 0, len(nums))
    return -1 if result == -1 else result[0]


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
