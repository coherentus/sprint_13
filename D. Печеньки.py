def check(zhadn, sizes):
    for _ in range(0, len(sizes)):
        cur_size = sizes.pop(0)
        if cur_size >= zhadn:
            return True
    return False    


def main():
    count_chldrn = int(input())
    f_zh = list(map(int, input().split()))
    count_coocie = int(input())
    sizes = list(map(int, input().split()))

    f_zh.sort()
    sizes.sort()

    count = 0
    idx = 0
    for zh in f_zh:
        if check(zh, sizes):
            count += 1
    
    print(count)


if __name__ == '__main__':
    main()
