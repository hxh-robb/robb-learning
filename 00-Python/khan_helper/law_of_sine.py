#!/usr/bin/env python

import math
import sys
from trig import d2r,r2d,r

def calc_case1(a_alpha,a_beta,s_alpha):
  a_alpha=float(a_alpha)
  a_beta=float(a_beta)
  a_gamma=180-a_alpha-a_beta
  s_alpha=float(s_alpha)
  s_beta=math.sin(d2r(a_beta))*s_alpha/math.sin(d2r(a_alpha))
  s_gamma=math.sin(d2r(a_gamma))*s_alpha/math.sin(d2r(a_alpha))
  return (r(a_alpha),r(s_alpha),r(a_beta),r(s_beta),r(a_gamma),r(s_gamma))

def calc_case2(a_alpha,a_beta,s_gamma):
  a_alpha=float(a_alpha)
  a_beta=float(a_beta)
  a_gamma=180-a_alpha-a_beta
  s_gamma=float(s_gamma)
  return calc_case1(a_gamma, a_beta, s_gamma)

def print_result(result):
  print 'sin(%.2f) - %.2f' % result[0:2]
  print 'sin(%.2f) - %.2f' % result[2:4]
  print 'sin(%.2f) - %.2f' % result[4:]

def main():
  if len(sys.argv) < 3:
    print 'Usage:'
    print '$angle_alpha $angle_beta $side_alpha'
    print 'A $angle_alpha $angle_beta $side_gamma'
    sys.exit(1)

  if 'A' not in sys.argv:
    print_reult(calc_case1(*tuple(sys.argv[1:])))
  elif 'A' in sys.argv:
    print_result(calc_case2(*tuple(sys.argv[2:])))
  else:
    print 'todo'

if __name__ == '__main__':
  main()
