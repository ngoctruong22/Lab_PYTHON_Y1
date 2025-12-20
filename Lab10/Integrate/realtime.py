import timeit
import math
from Integrate.integrate import integrate


def benchmark():
    """Запустите тесты производительности для нескольких значений n_iter и выведите результаты."""
    n_values = [1, 10, 100, 1000, 10000]
    for n in n_values:
        t = timeit.timeit(lambda: integrate(math.sin, 0, math.pi, n_iter=n), number=1000)
        print(f"Время выполнения при i_iter={n}: {t:.6f} s")


if __name__ == "__main__":
    benchmark()