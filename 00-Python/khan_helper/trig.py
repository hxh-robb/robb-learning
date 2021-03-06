#!/usr/bin/env python

import math

def prompt():
  print '$a = oppsite of angle $alpha'
  print '$b = oppsite of angle $beta'
  print '$c = oppsite of angle $gamma'
  print '----------'

def print_result(result):
  print '%.2f degree - oppsite: %.2f' % result[0:2]
  print '%.2f degree - oppsite: %.2f' % result[2:4]
  print '%.2f degree - oppsite: %.2f' % result[4:]

# degree to radian
def d2r(degree):
  return degree * math.pi / 180

# radian to degree
def r2d(radian):
  return radian * 180 / math.pi

# round
def r(value):
  # return round( value * 10000 ) / 10000
  return value

# sine(degree)
def sin(degree):
  return r(math.sin(d2r(degree)))

# cosine(degree)
def cos(degree):
  return r(math.cos(d2r(degree)))

# tangent(degree)
def tan(degree):
  return r(math.tan(d2r(degree)))

# sine^-1(ratio) => degree
def asin(ratio):
  return r(r2d(math.asin(ratio)))

# cosine^-1(ratio) => degree
def acos(ratio):
  return r(r2d(math.acos(ratio)))

# tangent^-1(ratio) => degree
def atan(ratio):
  return r(r2d(math.atan(ratio)))

# positive square root
def sqrt(value):
  if value < 0 : return 'todo'
  return math.sqrt(value)
