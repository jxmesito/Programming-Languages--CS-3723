import sys

def mmm(args):
  smallPos = 100000000
  largeNeg = -100000000
  for arg in args:
    n = int(arg)

    if 0 < n < smallPos:
    	smallPos = n;
    if largeNeg < n < 0:
    	largeNeg = n;
  return (smallPos, largeNeg)

smallPos,largeNeg = mmm(sys.argv[1:])
print("Smallest positive=%d Largest negative=%d" % (smallPos, largeNeg))
