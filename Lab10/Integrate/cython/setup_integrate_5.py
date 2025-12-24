from setuptools import setup
from Cython.Build import cythonize

file_path_5 = r"F:\Lab10\Integrate\cython\integrate_5_nogil.pyx"
setup(
    ext_modules=cythonize(
        file_path_5,
        annotate=True
    )
)