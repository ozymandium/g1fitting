from setuptools import setup, Extension
import os


g1fitting_ext_mod = Extension("g1fitting", 
  sources = [
    os.path.join('g1fitting', 'g1fittingmodule.cpp'),
  ],
  include_dirs = [
    os.path.join('g1fitting'),
  ],
  libraries = [
    "boost_python",
  ],
)

setup(
  name = "g1fitting",
  ext_modules = [
    g1fitting_ext_mod
  ],
)