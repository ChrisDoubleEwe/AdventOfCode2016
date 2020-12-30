import re
import string

rooms = []

with open("04_input.txt") as f:
  for line in f:
    match = re.search('([a-z\-]*)([0-9]*)\[([a-z]*)]', line)
    orig_name = match.group(1)
    name=match.group(1).replace('-','')
    id=int(match.group(2))
    checksum=match.group(3)
    room = []
    room.append(name)
    room.append(id)
    room.append(checksum)
    room.append(orig_name)
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

valid_rooms = []
result = 0
for r in rooms:
  if get_checksum(r[0]) == r[2]:
    valid_rooms.append(r)



for r in valid_rooms:
  id = r[1]
  enc = r[3]
  for i in range(0, id):
    this_enc = ''
    for c in enc:
      if c == ' ' or c == '-':
        this_enc += ' '
        continue
      c_val = string.lowercase.index(c)
      c_val += 1
      if c_val > 25:
        c_val = 0
      this_enc += string.lowercase[c_val] 
      enc = this_enc
  if "pole" in enc:
    print enc + " :: " + str(r[1])
