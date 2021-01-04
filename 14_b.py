import re
from printf import printf
import hashlib


salt = 'abc'
salt = 'zpqevtbw'

def get_hash(h):
  for i in range(0, 2017):
    tmp = h
    h = hashlib.md5(tmp.encode('utf-8')).hexdigest()
  return h
    

def test_me(h, i):
  found_c = ''
  regex = re.compile(r'([abcdef0-9])\1{2}')
  g = re.search(regex, h)

  if g:
     found_c = g.group()[0]
  if found_c == '':
    return False

  test = found_c+found_c+found_c+found_c+found_c
  for x in range(i+1, i+1001):
    test_hash = get_hash(salt+str(x))
    if test in test_hash:
      return True

  return False


keys = 0
i = 0
while keys < 64:
  print "Checking " + str(i)
  test = salt+str(i)
  hash = get_hash(test)

  if test_me(hash, i):
    keys += 1
    print "  Found key " + str(keys) + " at " + str(i)
  if keys == 64:
    print i
  i += 1


