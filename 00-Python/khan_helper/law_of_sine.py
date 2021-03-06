#!/usr/bin/env python

###
# a = oppsite of angle alpha
# b = oppsite of angle beta
# c = oppsite of angle gamma
###
# Law of sine:
# sin(alpha)/a = sin(beta)/b = sin(gamma)/c
###

import sys
from trig import *

def calc_case1(alpha,beta,a):
  alpha=float(alpha)
  beta=float(beta)
  a=float(a)
  # Solving
  gamma = 180 - alpha - beta
  b = sin(beta)  * a / sin(alpha)
  c = sin(gamma) * a / sin(alpha)
  return ( alpha, a, beta, b, gamma, c )

def calc_case2(alpha,beta,c):
  alpha=float(alpha)
  beta=float(beta)
  c=float(c)
  # Solving
  gamma = 180 - alpha - beta
  a = sin(alpha) * c / sin(gamma)
  b = sin(beta)  * c / sin(gamma)
  return ( alpha, a, beta, b, gamma, c )

def calc_case3(alpha,a,b):
  alpha=float(alpha)
  a=float(a)
  b=float(b)
  # Solving
  beta = asin( b * sin(alpha) / a )
  gamma = 180 - alpha - beta
  c = sin(gamma) * a / sin(alpha)
  return ( alpha, a, beta, b, gamma, c )

def main():
  prompt()
  
  if len(sys.argv) < 4:
    print 'Usage:'
    print '$alpha $beta $a'
    print 'A $alpha $beta $c'
    print 'B $alpha $a $b'
    sys.exit(1)

  if 'A' not in sys.argv and 'B' not in sys.argv:
    print_result(calc_case1(*tuple(sys.argv[1:])))
  elif 'A' in sys.argv:
    print_result(calc_case2(*tuple(sys.argv[2:])))
  elif 'B' in sys.argv:
    print_result(calc_case3(*tuple(sys.argv[2:])))
  else:
    print 'todo'

if __name__ == '__main__':
  main()
