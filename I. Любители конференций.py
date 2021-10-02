def main():
    count_persons = int(input())
    pers_id_hsc = map(int, input().split())
    k_count = int(input())
    count_id = dict()
    for hsc_id in pers_id_hsc:
        if hsc_id in count_id:
            count_id[hsc_id] += 1
        else:
            count_id[hsc_id] = 1
    res = list()
    for key, val in count_id.items():
        res.append([-val, key])
    res.sort()
    res = res[:k_count]
    res = [row[1] for row in res]
    print(*res)


if __name__ == '__main__':
    main()
