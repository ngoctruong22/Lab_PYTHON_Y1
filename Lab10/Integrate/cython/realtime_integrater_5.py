import timeit
import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from integrate_5_nogil import integrate_cy_nogil
from integrate_4 import integrate_cy


def benchmark_threads():
    """Сравнение многопоточности с noGIL"""
    n_threads = [2, 4, 6, 8]

    for n in n_threads:
        def run():
            with ThreadPoolExecutor(max_workers=n) as ex:
                futures = [
                    ex.submit(integrate_cy_nogil, 0, math.pi, 1000 // n)
                    for _ in range(n)
                ]
                return sum(f.result() for f in futures)

        t = timeit.timeit(run, number=3)
        print(f"noGIL threads={n}: {t:.6f} s")


def benchmark_processes():
    """Сравнение с мультипроцессной версией"""
    n_jobs = [2, 4, 6, 8]

    for n in n_jobs:
        def run():
            with ProcessPoolExecutor(max_workers=n) as ex:
                futures = [
                    ex.submit(integrate_cy, 0, math.pi, 1000 // n)
                    for _ in range(n)
                ]
                return sum(f.result() for f in futures)

        t = timeit.timeit(run, number=3)
        print(f"processes={n}: {t:.6f} s")


if __name__ == "__main__":
    print("noGIL threads")
    benchmark_threads()

    print("\nprocesses (cython)")
    benchmark_processes()