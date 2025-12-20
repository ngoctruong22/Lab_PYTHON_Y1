# integrate_4.pyx
# cython: boundscheck=False, wraparound=False, cdivision=True, language_level=3

cimport cython
from libc.math cimport sin

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef double integrate_cy(double a, double b, int n_iter):
    """Вычисляет приближённый интеграл функции sin(x) на отрезке [a, b]
    методом левых прямоугольников с n_iter разбиениями.

    Возвращает double.
    """
    if n_iter <= 0:
        raise ValueError("n_iter must be positive")

    return _integrate_cy_nogil(a, b, n_iter)


cdef inline double _integrate_cy_nogil(double a, double b, int n_iter) nogil:
    cdef double acc = 0.0
    cdef double step = (b - a) / n_iter
    cdef int i
    cdef double x

    for i in range(n_iter):
        x = a + i * step
        acc += sin(x) * step

    return acc