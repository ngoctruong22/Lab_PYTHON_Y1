import matplotlib.pyplot as plt
from benchmark import benchmark
from lab06 import gen_bin_tree_recursive
from lab06 import gen_bin_tree_nonrecursive


def main():
    heights = list(range(1, 20, 1))
    res_recursive = []
    res_nonrecursive = []

    for height in heights:
        res_recursive.append(benchmark(lambda: gen_bin_tree_recursive(height), number=1000))
        res_nonrecursive.append(benchmark(lambda: gen_bin_tree_nonrecursive(height), number=1000))
        # Визуализация
    plt.plot(res_recursive, label="Рекурсивный метод")
    plt.plot(res_nonrecursive, label="Нерекурсивный метод")
    plt.xlabel("Высота дерева (n)")
    plt.ylabel("Время")
    plt.title("Сравнение скорости построения дерева")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
