#!/usr/bin/env python

###
# a = oppsite of angle alpha
# b = oppsite of angle beta
# c = oppsite of angle gamma
###
# Law of cosine:
# c^2 = a^2 + b^2 + 2ab*cos(gamma)
###

#import math
import sys
from trig import *

def calc_case1(a,b,gamma):
  a=float(a)
  b=float(b)
  gamma=float(gamma)
  # Solving
  c = sqrt( a*a + b*b - 2*a*b*cos(gamma) )
  alpha  = acos( (a*a - b*b - c*c) / (-2*b*c) )
  beta = 180 - alpha - gamma
  return ( alpha, a, beta, b, gamma, c )

def calc_case2(a,b,c):
  a=float(a)
  b=float(b)
  c=float(c)
  alpha = acos( (a*a - b*b - c*c) / (-2*b*c) )
  beta = acos( (b*b - a*a - c*c) / (-2*a*c) )
  gamma = 180 - alpha - beta
  return ( alpha, a, beta, b, gamma, c )
  #theta=math.acos((c*c-b*b-a*a)/(-2*a*b))
  #return r(r2d(theta))

def main():
  prompt()
  
  if len(sys.argv) < 4:
    print 'Usage:'
    print 'calculate side = $a $b $gamma'
    print 'calculate angle = A $a $b $c'
    sys.exit(1)
  
  if 'A' not in sys.argv:
    print_result(calc_case1(*tuple(sys.argv[1:])))
  elif 'A' in sys.argv:
    print_result(calc_case2(*tuple(sys.argv[2:])))
  else:
    print 'todo'

if __name__ == '__main__':
  main()
