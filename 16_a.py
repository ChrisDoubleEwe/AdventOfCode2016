import re
from printf import printf
import hashlib

input = '01000100010010111'

length = 272
length = 35651584

def checksum(x):
  result = ''
  first = ''
  second = ''
  for c in x:
    if first == '':
      first = c
      continue
    else:
      second = c
      if first == second:
        result += '1'
      else:
        result += '0'
    first = ''
  #print len(result)
  if len(result)%2 == 1:
    #print 'Odd: ' + result
    return result
  else:
    #print 'Even: ' + result
    return checksum(result)

 

def reverse(x):
  result = ''
  x_rev = x[::-1]
  for c in x_rev:
    if c == '0':
      result += '1'
    else: 
      result += '0'
  return result

a = input
#print a
while len(a) < length:
  b = a + '0' + reverse(a)
  a = b
  #print a

result = ''
for x in range(0, length):
  result += a[x]

#print result
#print len(result)

csum = checksum(result)
print csum  
