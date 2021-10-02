def main():
    s_string = input()
    t_string = input()
    len_t = len(t_string)
    idx = 0
    res = False
    for ch in s_string:
        try:
            new_idx = t_string.index(ch, idx)
            idx = new_idx + 1
            res = True
        except ValueError:
            res = False
            break
    if len(s_string) == 0:
        res = True
    print(res)


if __name__ == '__main__':
    main()
