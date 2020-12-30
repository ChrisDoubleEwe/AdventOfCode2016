import re
import hashlib

#door = 'abc'
door = 'ugkcyxxp'
password = ['-', '-', '-', '-', '-', '-', '-', '-']
passcount = 0

result = hashlib.md5(b'abc3231929') 

i = 0
while '-' in password:
  x = door + str(i)
  x_hash = hashlib.md5(x)
  if x_hash.hexdigest()[:5] == '00000':
    pos = x_hash.hexdigest()[5:6]
    char = x_hash.hexdigest()[6:7]
    if pos in '01234567':
      if password[int(pos)] == '-':
        password[int(pos)] = char
        print ''.join(password)
  i+=1



print "--------------"
print ''.join(password)


