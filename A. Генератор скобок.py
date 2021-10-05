def is_correct_bracket_seq(sequense: str) -> bool:
    left_brackets = ('(',)
    brackets = {'(': ')'}
    stack = []
    if sequense == '':
        return True
    if sequense[0] not in left_brackets:
        return False
    for item in sequense:
        if item in left_brackets:
            stack.append(item)
        else:
            if len(stack) == 0:
                return False
            answer = stack.pop()
            if brackets[answer] != item:
                return False
    if len(stack):
        return False
    return True


def main():
    count = int(input())
    full = 2 ** (count * 2)
    # двоичные числа
    binaries = [str(bin(x)) for x in range(full)]
    # print('двоичные числа', binaries)
    binaries = list(map(lambda x: x[2:], binaries))
    # print('строки без 0b', binaries)
    for i in range(len(binaries)):
        zer_out = count * 2 - len(binaries[i])
        binaries[i] = '0' * zer_out + binaries[i]
        res = ''
        for ch in binaries[i]:
            if ch == '0':
                res += '('
            else:
                res += ')'
        binaries[i] = res
        # print('скобки полной длины', res)

    result = []
    for seq in binaries:
        # print('посылка в проверку', seq)
        # print('проверка', is_correct_bracket_seq(seq))
        if is_correct_bracket_seq(seq):
            # print('корректные скобки', seq)
            result += [seq]
            # print(result)

    print(*result, sep='\n')


if __name__ == '__main__':
    main()
