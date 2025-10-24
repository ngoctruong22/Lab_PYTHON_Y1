import timeit


def benchmark(func, number=1):
    """ Возвращает среднее время создания дерева."""
    times = timeit.timeit(lambda: func, number=number)
    return times / number
