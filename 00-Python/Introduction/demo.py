#!/usr/bin/env python
""" MAMAMAMAM """

# import sys
import time

def main():
  ''' entry '''
  return

def aaaa():
  ''' something here '''
  print 'Test pylint'

def repeat(text, exclaim):
  """ Repeat """
  # if not(text == 'A') and len(text) == 1:
  if text == 'A':
    result = text * 3
  else:
    result = text * 5
  if exclaim:
    result += '!!!'
  return result

def test_performance():
  ''' test something '''
  size = 1

  lap1 = time.time()
  var1 = [None] * size

  lap2 = time.time()
  # var2 = var1[:]
  # var2[-1] = 7
  # var2 = var1[:]
  var2 = var1

  lap3 = time.time()
  same = var1 == var2

  end = time.time()

  print '\
  total = %f,\
  init var1 = %f,\
  init var2 = %f,\
  comparison between var1 and var2 = %f,\
  same = %s' % (
      end - lap1,
      lap2 - lap1,
      lap3 - lap2,
      end - lap3,
      same
  )

if __name__ == '__main__':
  test_performance()
