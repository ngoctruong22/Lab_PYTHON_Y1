import math


# итерация 1
# Dấu * ngăn cách giữa các positional arguments (tham số theo vị trí) và keyword-only arguments (tham số phải truyền bằng tên).
def integrate(f, a, b, *, n_iter=100000):
    """
    Вычислите приближённый интеграл функции f на интервале [a, b] методом левого прямоугольника.

      Параметры:
      f : callable: Функция одной переменной, которую требуется интегрировать.
      a : float: Левая граница.
      b : float: Правая граница.
      n_iter : int: Количество подотрезков.

      Returns: ->float
          Приблизительное значение интеграла.
    - написать тесты для функции (2 штуки тут)
    - + тесты с помощью Unittest / py.test
    >>> round(integrate(math.cos, 0, math.pi / 2, n_iter=1000), 5)  #round(number, ndigits: Số chữ số thập phân muốn giữ lại (tùy chọn))
    1.00079
    >>> round(integrate(math.sin,0,math.pi,n_iter=1000),3)
    2.0
    >>> round(integrate(lambda x: x**2, 0, 1, n_iter=1000), 1)
    0.3
    """
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc
# print(integrate(math.sin, 0, math.pi, n_iter=1000))

if __name__ == "__main__":
    import doctest
    doctest.testmod() # Chạy doctest trong module này

