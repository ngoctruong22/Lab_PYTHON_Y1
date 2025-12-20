import timeit
import math
from integrate_4 import integrate_cy

def benchmark():
    """Сравнение производительности разного количества потоков"""
    print("Cython (оптимизированная версия)")
    t = timeit.timeit(
        lambda: integrate_cy(0, math.pi, 1000),
        number=1000
    )
    print(f"Время выполнения: {t:.6f} s")

if __name__ == "__main__":
    benchmark()