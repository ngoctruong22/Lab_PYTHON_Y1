import timeit
import math
from integrate_threaded import integrate_threaded

def benchmark():
    """Сравнение производительности разного количества потоков"""
    n_threads = [2, 4, 6, 8]
    for n in n_threads:
        t = timeit.timeit(lambda: integrate_threaded(math.sin, 0, math.pi, n_iter=1000, n_threads=n), number=1000)
        print(f"Время выполнения при n_thread={n}: {t:.6f} s")


if __name__ == "__main__":
    benchmark()