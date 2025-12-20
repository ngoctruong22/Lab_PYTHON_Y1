import math
from typing import Callable
import threading
from integrate import integrate



def integrate_threaded(f: Callable[[float], float], 
                      a: float, 
                      b: float, 
                      *, 
                      n_iter: int = 10000, 
                      n_threads: int = 4) -> float:
    """
    Вычисляет приближённый интеграл функции f на отрезке [a, b] методом левых прямоугольников
    с параллельным разбиением по потокам.

    Параметры:
        f : callable
            Функция одной переменной для интегрирования.
        a : float
            Левая граница интервала.
        b : float
            Правая граница интервала.
        n_iter : int
            Общее число подотрезков (разбиений).
        n_threads : int
            Количество потоков для параллельного вычисления.

    Возвращает:
        float
            Приблизительное значение интеграла.

    Исключения:
        ValueError
            Если n_iter < n_threads.

    - написать тесты для функции (2 штуки тут)
    - + тесты с помощью Unittest / py.test

    >>> round(integrate_threaded(math.cos, 0, math.pi / 2, n_iter=1000, n_threads=4), 5)
    1.00079
    >>> round(integrate_threaded(math.sin, 0, math.pi, n_iter=1000, n_threads=4), 3)
    2.0
    >>> round(integrate_threaded(lambda x: x**2, 0, 1, n_iter=1000, n_threads=4), 1)
    0.3
    """
    if n_iter < n_threads:
        raise ValueError("Invalid parameters")
    
    # Chia đoạn [a, b] thành n_threads phần
    chunk_width = (b - a) / n_threads
    n_iter_per_thread = n_iter // n_threads

    # Dùng list để lưu kết quả từ các luồng
    results = [0.0] * n_threads
    threads = []

    # Hàm wrapper để lưu kết quả
    def integrate_chunk(thread_index, func, start, end, n_iter_chunk):
        # print(f"Thread {thread_id} is integrating from {start} to {end} with {n_iter_chunk} iterations.")
        results[thread_index] = integrate(func, start, end, n_iter=n_iter_chunk)

    # Tạo và khởi động các luồng
    for i in range(n_threads):
        chunk_a = a + i * chunk_width
        chunk_b = a + (i + 1) * chunk_width
        
        thread = threading.Thread(
            target=integrate_chunk,
            args=(i, f, chunk_a, chunk_b, n_iter_per_thread)
        )
        threads.append(thread)
        thread.start()  # QUAN TRỌNG: phải start(): bắt đầu luồng
    
    # Chờ tất cả luồng hoàn thành
    for thread in threads:
        thread.join()  # QUAN TRỌNG: phải join(): chờ luồng kết thúc
    # Tính tổng kết quả
    return sum(results)
# print(integrate_threaded(math.sin, 0, math.pi, n_iter=10000, n_threads=4))
