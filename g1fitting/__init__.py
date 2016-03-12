import g1fitting_


def build_clothoid(x0, y0, theta0, x1, y1, theta1):
  """
  Given two 2D poses (point and orientation), construct a clothoid which passes
  though the given points with a tangent line at the given angle at those 
  intersections.

  Parameters
  ----------
  x0: x-coordinate of starting point
  y0: y-coordinate of starting point
  theta0: right-handed angle in radians from x-axis to y-axis of the starting 
          clothoid orientation
  x0: x-coordinate of ending point
  y0: y-coordinate of ending point
  theta0: right-handed angle in radians from x-axis to y-axis of the ending 
          clothoid orientation
  
  Returns
  -------
  k: initial curvature
  dk: 1st derivative of curvature with respect to arc length
  L: necessary arc length from point 0 to point 1
  """
  return g1fitting_.build_clothoid(x0, y0, theta0, x1, y1, theta1)


def points_on_clothoid(x0, y0, theta0, k, dk, L, npts):
  """
  Evenly sample a clothoid along its arc length

  Parameters
  ----------
  x0: x-coordinate of starting point
  y0: y-coordinate of starting point
  theta0: right-handed angle in radians from x-axis to y-axis of the starting 
          clothoid orientation
  k: initial curvature
  dk: 1st derivative of curvature with respect to arc length
  L: necessary arc length from point 0 to point 1
  npts: number of points to sample

  Returns
  -------
  list of length 2 tuples representing the 2D sampled points

  """
  return g1fitting_.points_on_clothoid(x0, y0, theta0, k, dk, L, npts)