def quick_sort(players):
    """Сортировка массива по трём составлющим.
    
    Args:
        players (list[str, int, int]) - Имя, баллы, штраф.
    Returns:
        result (list[str]) - Имя.
    Правила сортировки - баллы по возрастанию, штраф по убыванию,
    имя по алфавиту.
    """
    pass

def main():
    count_item = int(input())
    items = ['', '', ''] * count_item
    for i in range(count_item):
        name, points, penalty = input().split()
        items[i] = [name, int(points), int(penalty)]
    
    result = quick_sort(items)
    print(result)


if __name__ == '__main__':
    main()

