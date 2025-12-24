from setuptools import setup
from Cython.Build import cythonize

file_path_4 = r"F:\Lab10\Integrate\cython\integrate_4.pyx"
setup(
    ext_modules=cythonize(
        file_path_4,
        annotate=True
    )
)