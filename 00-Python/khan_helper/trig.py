#!/usr/bin/env python

import math

# degree to radian
def d2r(degree):
  return degree * math.pi / 180

# radian to degree
def r2d(radian):
  return radian * 180 / math.pi

# round
def r(value):
  return round( value * 100 ) / 100
