import re

rooms = []

with open("04_input.txt") as f:
  for line in f:
    match = re.search('([a-z\-]*)([0-9]*)\[([a-z]*)]', line)
    name=match.group(1).replace('-','')
    id=int(match.group(2))
    checksum=match.group(3)
    room = []
    room.append(name)
    room.append(id)
    room.append(checksum)
    rooms.append(room)

def get_checksum(x):
  max = 0
  letters = {}
  for l in x:
    if l in letters.keys():
      letters[l] += 1
    else:
      letters[l] = 1
    if letters[l] > max:
      max = letters[l]

  checksum = ''
  for i in range(max, 0, -1):
    substring = ''
    for l in letters.keys():
      if letters[l] == i:
        substring += l
    sub_sorted=sorted(substring)

    if len(sub_sorted) > 0:
      for z in sub_sorted:
        checksum+=z

  return checksum[:5]

result = 0
for r in rooms:
  if get_checksum(r[0]) == r[2]:
    result += r[1]

print result



