from distutils.core import setup, Extension
import os
from distutils.sysconfig import get_config_vars

g1fitting_ext_mod = Extension("g1fitting", 
  sources=["g1fittingmodule.cpp"],
  include_dirs=["."],
  extra_compile_args=["-std=c++11"],
  libraries=["boost_python"],
)

# unwanted_flags = [
#   '-Wstrict-prototypes'
#   '-Wuninitialized]'
# ]

# import distutils.sysconfig
# cfg_vars = distutils.sysconfig.get_config_vars()
# for key, value in cfg_vars.items():
#   if type(value) == str:
#     for uwf in unwanted_flags:
#       cfg_vars[key] = value.replace(uwf, "")

setup(name="G1Fitting", ext_modules=[g1fitting_ext_mod])