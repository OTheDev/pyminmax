from setuptools import setup, Extension

module = Extension('_pyminmax', sources=["src/pyminmax/_pyminmaxmodule.c"])

setup(ext_modules=[module])
