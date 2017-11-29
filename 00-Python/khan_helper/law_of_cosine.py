#!/usr/bin/env python

import math
import sys
from trig import d2r,r2d,r

# given side a, side b and the angle between both sides, get the length of side c
def calc_side(a,b,angle):
  a=float(a)
  b=float(b)
  angle=float(angle)
  #return (a*a,b*b,d2r(angle))
  c=math.sqrt(a*a+b*b-2*a*b*math.cos(d2r(angle)))
  return r(c)

def calc_angle(a,b,c):
  a=float(a)
  b=float(b)
  c=float(c)
  theta=math.acos((c*c-b*b-a*a)/(-2*a*b))
  return r(r2d(theta))

def main():
  if len(sys.argv) < 3:
    print 'Usage:'
    print 'calculate side = $a $b $angle'
    print 'calculate angle = A $a $b $c'
    sys.exit(1)
  
  if 'A' not in sys.argv:
    print calc_side(*tuple(sys.argv[1:]))
  elif 'A' in sys.argv:
    print calc_angle(*tuple(sys.argv[2:]))
  else:
    print 'todo'

if __name__ == '__main__':
  main()
