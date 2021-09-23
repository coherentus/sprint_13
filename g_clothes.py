def sort_clothes(arr, len):
    colors = [0, 0, 0]
    colors[0] = arr.count(0)
    colors[1] = arr.count(1)
    colors[2] = arr.count(2)
    index = 0
    for i in range(3):
        for _ in range(colors[i]):
            arr[index] = i
            index += 1
    return arr

def main():
    count_item = int(input())
    items = list(map(int, input().split()))
    
    result = sort_clothes(items, count_item)
    print(*result)

if __name__ == '__main__':
    main()
