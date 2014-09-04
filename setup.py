from setuptools import setup, Extension, find_packages

ext = Extension(
    '_pygilstate_check',
    sources=['_pygilstate_check.c'],
    extra_compile_args=['-DNDEBUG=1', '-O3'],
)

setup(
    name='PyGILState_Check',
    version=0.1,
    author='Pankaj Pandey',
    author_email='pankaj86@gmail.com',
    description='PyGILState_Check2 for Python',
    ext_modules=[ext],
    py_modules=['pygilstate_check'],
    data_files=[('include', ['pygilstate_check.h'])],
    packages=find_packages(),
    license='MIT',
    zip_safe= False,
)
