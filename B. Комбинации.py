"""На клавиатуре старых мобильных телефонов каждой цифре соответствовало
несколько букв. Примерно так:

2:'abc',
3:'def',
4:'ghi',
5:'jkl',
6:'mno',
7:'pqrs',
8:'tuv',
9:'wxyz'

Вам известно в каком порядке были нажаты кнопки телефона,
без учета повторов. Напечатайте все комбинации букв, которые можно набрать
такой последовательностью нажатий.
Формат ввода
На вход подается строка, состоящая из цифр 2-9 включительно. Длина строки не
превосходит 10 символов.
Формат вывода
Выведите все возможные комбинации букв через пробел.
"""
def main():
    symbolls = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }
    in_str = input()
    out_smb = [None] * len(in_str)
    for i in range(len(in_str)):
        cifer_smb = [*symbolls[int(in_str[i])]]
        out_smb[i] = cifer_smb
    out_str = out_smb[0]
    for k in range(1, len(out_smb)):
        cur_len = len(out_smb[k])
        ott_str = list()
        for i in range(len(out_str)):
            cur_out = [out_str[i]] * cur_len
            for j in range(cur_len):
                cur_out[j] = cur_out[j] + out_smb[k][j]
            ott_str.extend(cur_out)
            print(ott_str)
        out_str = ott_str

    
    print(*out_str)


if __name__ == '__main__':
    main()
