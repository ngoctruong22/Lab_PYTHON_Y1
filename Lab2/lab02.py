def main():
    """
    Ввод значений с клавиатуры для формирования
    списка, по которому мы ищем искомое число и
    искомого числа
    (опционально) предложить пользователю сформировать
    список вручную с клавиатуры

    __вызов функции guess-number с параметрами: __
      - искомое число (target)
      - список, по-которому идем
      - тип поиска (последовательный, бинарный)

    __вывод результатов на экран__
    return:
    """

    target = int(input('Введите target: '))
    start_range = int(input('Введите начало диап: '))
    end_range = int(input('Введите конец диап: '))
    d = list(range(start_range, end_range + 1))
    type_search = (input('Алгоритм, который вы хотите найти: '))
    res = guess_number(target, d, type=type_search)
    print(f'{res}')


def guess_number(target: int, lst: [int], type: str) -> list[int | None, int]:
    comparisons = 0

    # ищем число последовательно
    if type == 'seq':
        print(lst)
        for i in range(len(lst)):
            comparisons += 1
            if lst[i] == target:
                return [lst[i], comparisons]

        return [None, comparisons]

    # ищем число с помощью алгоритма бинарного поиска
    elif type == 'bin':
        left = 0
        right = len(lst) - 1
        while left <= right:
            mid = int((left + right) / 2)
            comparisons += 1
            if target == lst[mid]:
                return [lst[mid], comparisons]
            elif target < lst[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return [None, comparisons]


if __name__ == '__main__':
    main()
