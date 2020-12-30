import re
import hashlib

#door = 'abc'
door = 'ugkcyxxp'
password = ''

result = hashlib.md5(b'abc3231929') 

i = 0
while len(password) < 8:
  x = door + str(i)
  x_hash = hashlib.md5(x)
  if x_hash.hexdigest()[:5] == '00000':
    password += x_hash.hexdigest()[5:6]
    print str(len(password)) + " : " + password
  i+=1



print "--------------"
print password



