import concurrent.futures as ftres
from functools import partial
from integrate import integrate
import math

def integrate_async(f, a, b, *, n_jobs=2, n_iter=1000):
    """  
    Параллельное вычисление интеграла с использованием процессов
    (ProcessPoolExecutor).

    Parameters
    ----------
    f : callable
        Интегрируемая функция
    a, b : float
        Границы интегрирования
    n_jobs : int
        Количество процессов
    n_iter : int
        Общее число итераций

    Returns
    -------
    float
        Приближённое значение интеграла
    """

    # tao ra pool voi so tien trinh la n_jobs
    executor = ftres.ThreadPoolExecutor(max_workers=n_jobs) # создаваемый пул тредов будет размера n_jobs

    # tao ra partial function de goi integrate voi cac tham so co san
    spawn = partial(executor.submit, integrate, f, n_iter = n_iter // n_jobs)   # partial позволяет "закрепить"
                                                                                # несколько аргументов
                                                                                # для удобства вызова функции ,
                                                                                # см. пример ниже
    step = (b - a) / n_jobs
    # for i in range(n_jobs):
    #   print(f"Работник {i}, границы: {a + i * step}, {a + (i + 1) * step}")

    #tao cac future de chay song dong
    fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]    # создаем потоки с помощью генератора
                                                                             # списков; partial позволил нам

    return sum(list(f.result() for f in ftres.as_completed(fs)))                     # as.completed() берет на вход список
                                                                                # фьючерсов и как только какой-то
                                                                                # завершился, возвращает результат
                                                                                # f.result(), далее, мы эти результаты
                                                                                # складываем

# print(integrate_async(math.sin, 0, math.pi))