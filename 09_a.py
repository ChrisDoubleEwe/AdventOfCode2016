import re
from printf import printf

data = 'ADVENT'
data = 'A(1x5)BC'
data = '(3x3)XYZ'
#data = 'A(2x2)BCD(2x2)EFG'
#data = '(6x1)(1x3)A'
data = 'X(8x2)(3x3)ABCY'
data = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
data = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'

my_data = ''

with open("09_input.txt") as f:
  for line in f:
    my_data += line.strip()

data = my_data


in_marker = 0
length = -1
marker = ''
final = ''

iter = 0
while (data.count('(') > 0): 
 iter += 1
 counter = data.count('(')
 print "Iteration: " + str(iter) + " bracket count: " + str(counter)
 for c in data:
  if in_marker == -1:
    if length > 0:
      repeat += c
      length -= 1
    if length == 0:
      for i in range(0, reps):
        final += repeat
      length = -1
      in_marker = 0
      continue
    if length == -1:
      final += c
    continue

  if in_marker == 0 and c != '(':
    final += c
    continue
  if in_marker == 0 and c == '(':
    in_marker = 1
    marker = ''
    continue
  if in_marker == 1 and c != ')':
    marker += c
    continue
  if in_marker == 1 and c == ')':
    in_marker = -1
    match = re.search('([0-9]*)x([0-9]*)', marker)
    length = int(match.group(1))
    reps = int(match.group(2))
    repeat = ''
    continue
 counter = final.count('(')    
 data = final
 final = ''

#print data
print len(data)
