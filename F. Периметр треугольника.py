def how_math(numbers: list):
    numbers.sort(reverse=True)
    for i in range(len(numbers)):
        first = numbers[i]
        for j in range(i + 1, len(numbers) - 1):
            second = numbers[j]
            for k in range(j + 1, len(numbers)):
                two_sum = second + numbers[k]
                if two_sum > first:
                    return two_sum + first


def main():
    _ = int(input())
    segments = list(map(int, input().split()))

    print(how_math(segments))


if __name__ == '__main__':
    main()
