import re
from printf import printf
import hashlib

discs = [[5, 4], [2, 1]]
discs = [[17, 5], [19, 8], [7, 1], [13, 7], [5, 1], [3,0] ]


consecutive_zeroes = 0
first = 0

i = -1
keep_going = 1
while keep_going == 1:
  i+=1
  print '-- ' + str(i) + ' ------'
  for x in discs:
    print x[1]

  print ' ++ ' + str(discs[consecutive_zeroes][1])
  if discs[consecutive_zeroes][1] == 0:
    if consecutive_zeroes == 0:
      first = i -1
    consecutive_zeroes += 1
    print "GOT ONE!"
  else:
    consecutive_zeroes = 0

  if consecutive_zeroes == len(discs):
    print "DONE!"
    keep_going = 0

  for z in range(0, len(discs)):
    discs[z][1] = (discs[z][1] + 1) % discs[z][0]


print "Result: drop at t = " + str(first)
