from pathlib import Path
from setuptools import setup
from Cython.Build import cythonize

# Use absolute path so script works no matter the current working directory
this_dir = Path(__file__).resolve().parent
pyx_path = this_dir / "integrate_4.pyx"

if not pyx_path.exists():
    raise FileNotFoundError(f"Could not find Cython source file: {pyx_path}")

setup(
    ext_modules=cythonize(
        str(pyx_path),
        annotate=True,
        compiler_directives={"language_level": "3"},
    )
)