def find_median(arr_1, arr_2, len_1, len_2):
    pass

def main():
    north_len = int(input())
    south_len = int(input())
    north = list(map(int, input().split()))
    south = list(map(int, input().split()))
    
    res = find_median(north, south, north_len, south_len)


    print(res)


if __name__ == '__main__':
    main()
