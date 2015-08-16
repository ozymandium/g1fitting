#ifndef G1FITTING_MODULE_HPP
#define G1FITTING_MODULE_HPP


#include "Clothoid.h"
#include "Clothoid.cpp"

#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
#include <boost/python/list.hpp>
#include <boost/python/iterator.hpp>
#include <boost/foreach.hpp>

#include <vector>


namespace py = boost::python;


template<class T>
py::list std_vector_to_py_list(const std::vector<T>& v)
{
    py::object get_iter = py::iterator<std::vector<T> >();
    py::object iter = get_iter(v);
    py::list l(iter);
    return l;
}


py::list
g1fitting_build_clothoid(
  double x0,
  double y0,
  double theta0,
  double x1,
  double y1,
  double theta1
)
{
  double k, dk, L;
  int res = Clothoid::buildClothoid(x0, y0, theta0, x1, y1, theta1, k, dk, L);
  py::list ret;
  ret.append(k);
  ret.append(dk);
  ret.append(L);
  ret.append(res);
  return ret;
}


py::list
g1fitting_points_on_clothoid(
  double x0,
  double y0,
  double theta0,
  double k,
  double dk,
  double L,
  uint npts
)
{
  std::vector<double> X(npts), Y(npts);
  int res = Clothoid::pointsOnClothoid(x0, y0, theta0, k, dk, L, npts, X, Y);
  py::list Xl, Yl;
  BOOST_FOREACH(const double& v, X) Xl.append(v);
  BOOST_FOREACH(const double& v, Y) Yl.append(v);
  py::list ret;
  ret.append(Xl);
  ret.append(Yl);
  ret.append(res);
  return ret;
}


BOOST_PYTHON_MODULE(g1fitting)
{
  py::def("build_clothoid", g1fitting_build_clothoid);
  py::def("points_on_clothoid", g1fitting_points_on_clothoid);
}

#endif