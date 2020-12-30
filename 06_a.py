import re

mess = []

first = 1
with open("06_input.txt") as f:
  for line in f:
    if first == 1:
      for x in range(0, len(line)-1):
        mess.append([])
        first = 0
    i = 0
    for c in line.strip():
      mess[i].append(c)
      i += 1


decode = ''

for x in mess:
  max = 0
  max_char = ''
  for c in 'abcdefghijklmnopqrstuvwxyz':
    cnt = x.count(c)
    if cnt > 0:
      if cnt > max:
        max_char = c
        max = cnt
  decode += max_char

print decode

