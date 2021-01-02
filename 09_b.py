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
data_weight = []
for c in data:
  data_weight.append(1) 


in_marker = 0
length = -1
marker = ''
final = ''


total_length = 0


idx = -1
for c in data:
  idx += 1
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
    total_length += data_weight[idx]
    continue
  if in_marker == 0 and c == '(':
    in_marker = 1
    marker = ''
    continue
  if in_marker == 1 and c != ')':
    marker += c
    continue
  if in_marker == 1 and c == ')':
    match = re.search('([0-9]*)x([0-9]*)', marker)
    length = int(match.group(1))
    reps = int(match.group(2))
    for i in range(idx+1, idx+1+length):
      data_weight[i]=data_weight[i]*reps
    in_marker = 0
    continue
print total_length
