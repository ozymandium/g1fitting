from setuptools import setup, Extension
import os


g1fitting_ext_mod = Extension("g1fitting_", 
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
  packages = [
    'g1fitting',
  ],
  version = '0.1.2',
  description = 'A package to create and sample C1 continuous clothoid curves.',
  author = 'Robert Cofield',
  author_email = 'robertgcofield@gmail.com',
  url = 'https://github.com/ozymandium/g1fitting',
  download_url = 'https://github.com/ozymandium/g1fitting/tarball/pypi',
  keywords = ['clothoid', 'curvature', 'curve', 'fitting'],
  ext_modules = [
    g1fitting_ext_mod
  ],
)