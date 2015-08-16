#include "Clothoid.h"

#include <math.h>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <unistd.h>
#include <vector>


/*print array*/
template <typename T>
std::string artoa(T array, int N) {
  std::ostringstream os;
  os << "{";
  for (int k = 0; k < N; k++) {
    os << array[k] << ", ";
  }
  os << "\b\b}";
  return os.str();
}


template <typename T>
std::string vectoa(std::vector<T> v) {
  std::ostringstream os;
  os << "[" << v.size() << "] {";
  for (auto vv : v) {
    os << vv << ", ";
  }
  os << "\b\b}";
  return os.str();
}


int main(int argc, char* argv[]) {

  double x0 = 0;
  double y0 = 0;
  double theta0 = M_PI/2.0;
  double x1 = 1;
  double y1 = 0.5;
  double theta1 = 0;

  size_t n = 10;

  double k;
  double dk;
  double L;

  int res = Clothoid::buildClothoid(x0, y0, theta0, x1, y1, theta1, k, dk, L);

  std::cout << "k: " << k << "\n"
            << "dk: " << dk << "\n"
            << "L: " << L << "\n";

  std::vector<double> X(10), Y(10);
  res = Clothoid::pointsOnClothoid(x0, y0, theta0, k, dk, L, 100, X, Y);
  std::cout << "X:\n" << vectoa(X) << "\n\n"
            << "Y:\n" << vectoa(Y) << "\n";

  return 0;
}