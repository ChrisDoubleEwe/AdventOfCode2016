import re
from printf import printf
import hashlib


salt = 'abc'
salt = 'zpqevtbw'



def test_me(h, i):
  found_c = ''
  for x in range(0, len(h)-2):
    c = h[x]
    d = h[x+1]
    e = h[x+2]
    if c == d == e and found_c == '':
      found_c = c
  if found_c == '':
    return False

  test = found_c+found_c+found_c+found_c+found_c
  for x in range(i+1, i+1001):
    test_hash = hashlib.md5((salt+str(x)).encode('utf-8')).hexdigest()
    if test in test_hash:
      return True

  return False


keys = 0
i = 0
while keys < 64:
  test = salt+str(i)
  hash = hashlib.md5(test.encode('utf-8')).hexdigest()

  if test_me(hash, i):
    keys += 1
    print "  Found key " + str(keys) + " at " + str(i)
  if keys == 64:
    print i
  i += 1


