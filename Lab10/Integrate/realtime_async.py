import timeit
import math
from integrate_async import integrate_async

def benchmark():
    """Сравнение производительности разного количества процессов"""
    n_jobs = [2, 4, 6, 8]
    for n in n_jobs:
        t = timeit.timeit(lambda: integrate_async(math.sin, 0, math.pi, n_jobs=n, n_iter=1000), number=1000)
        print(f"Время выполнения при n_jobs= {n}: {t:.6f} s")


if __name__ == "__main__":
    benchmark()