#!/usr/bin/env python

if __name__ == '__main__':
  
  import sys, os
  from math import pi
  from g1fitting import build_clothoid, points_on_clothoid
  import matplotlib.pyplot as plt
  
  x0 = 0.
  y0 = 0.
  theta0 = 0.

  x1 = 1.
  y1 = 1.
  theta1 = pi/2.0

  (k, dk, L, res1) = build_clothoid(x0, y0, theta0, x1, y1, theta1)
  (X, Y, res2) = points_on_clothoid(x0, y0, theta0, k, dk, L, 100)

  plt.figure()
  plt.plot(X,Y)
  plt.show()