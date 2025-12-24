# cython: boundscheck=False
# cython: wraparound=False
# cython: cdivision=True


from libc.math cimport sin
cimport cython
@cython.boundscheck(False)
@cython.wraparound(False)
def integrate_cy_nogil(double a, double b, int n_iter):
    cdef:
        double acc = 0.0
        double step = (b - a) / n_iter
        int i

    with nogil:
        for i in range(n_iter):
            acc += sin(a + i * step) * step

    return acc