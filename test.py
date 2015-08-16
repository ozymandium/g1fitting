#!/usr/bin/env python
import sys, os
from math import pi
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'build', 'lib.linux-x86_64-2.7'))
from g1fitting import build_clothoid, points_on_clothoid
import matplotlib.pyplot as plt
from ipdb import set_trace

x0 = 0.
y0 = 0.
theta0 = 0.

x1 = 1.
y1 = 1.
theta1 = pi/2.0

(k, dk, L, res1) = build_clothoid(x0, y0, theta0, x1, y1, theta1)
(X, Y, res2) = points_on_clothoid(x0, y0, theta0, k, dk, L, 100)
# set_trace()


plt.figure()
plt.plot(X,Y)
plt.show()