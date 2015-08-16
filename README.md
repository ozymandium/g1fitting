# g1fitting
Clothoid generation and sampling library, with Python wrapper

The library was originally written by
- Enrico Bertolazzi
- Dipartimento di Ingegneria Industriale
- Universita` degli Studi di Trento
- email: enrico.bertolazzi@unitn.it

An excellent MATLAB version of this, with many more features, exists on the MATLAB File Exchange [here](http://www.mathworks.com/matlabcentral/fileexchange/42113-g1-fitting-with-clothoids)

I've ported his MATLAB sampling function back to C++ and added a Python 2.7 wrapper for `Clothoid::buildClothoid` and `Clothoid::pointsOnClothoid`

## Build

#### C++ library
typical CMake operation: `mkdir build && cd build && cmake .. && make && ./test`

#### Python wrapper
Use the typical method: `python setup.py build && python test.py`. This does not require the C++ library to be built, and operates without the CMake build system.

Note that this has only been tested on Linux
