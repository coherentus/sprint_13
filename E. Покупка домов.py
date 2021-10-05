def how_many(full_sum, sums: list):
    sums.sort()
    count = 0
    for one_price in sums:
        full_sum -= one_price
        if full_sum >= 0:
            count += 1
            continue
        else:
            break
    return count


def main():
    num, budget = map(int, input().split())

    houses = list(map(int, input().split()))

    print(how_many(budget, houses))


if __name__ == '__main__':
    main()
