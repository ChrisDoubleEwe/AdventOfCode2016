import re
from printf import printf
import hashlib

elfs = []
num_elfs = 5
num_elfs = 3012210

for i in range(0, num_elfs):
  elfs.append(1)


exit = 0
while exit == 0:
  for x in range(0, num_elfs):
    if elfs[x] == 0:
      continue
    next_elf = (x + 1) % num_elfs
    gifts = 0
    while next_elf != x and gifts == 0:
      gifts = elfs[next_elf]
      if gifts > 0:
        elfs[x] += gifts
        elfs[next_elf] = 0
      next_elf = (next_elf + 1) % num_elfs
    if gifts == 0:
      exit = 1
      break
    
for i in range(0, num_elfs):
  if elfs[i] > 0:
    print "Elf " + str(i+1) + " wins"
    
