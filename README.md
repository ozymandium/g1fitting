# g1fitting
Clothoid generation and sampling library, with Python wrapper

The library was originally written by the authors of the work published [here](http://onlinelibrary.wiley.com/doi/10.1002/mma.3114/abstract). For questions regarding the underlying algorithm, contact Enrico Bertolazzi, _Universita` degli Studi di Trento_ (Dipartimento di Ingegneria Industriale). Email: enrico.bertolazzi@unitn.it

An excellent MATLAB version of this, with many more features, exists on the MATLAB File Exchange [here](http://www.mathworks.com/matlabcentral/fileexchange/42113-g1-fitting-with-clothoids)

I've ported his MATLAB sampling function back to C++ and added a Python 2.7 wrapper for `Clothoid::buildClothoid` and `Clothoid::pointsOnClothoid`. The MATLAB function `G1spline`, which computes a spline for `N > 2` points, has not yet been ported.

## Build/install

Installation is available via PyPI: `pip install g1fitting`

The `pypi` branch has all code related to that.

### Source build

#### C++ library
typical CMake operation: `mkdir build && cd build && cmake .. && make install && ./test`

#### Python wrapper
Use the typical method: `python setup.py install && python test.py`. This does not require the C++ library to be built, and operates without the CMake build system.

Note that this has only been tested on Linux

