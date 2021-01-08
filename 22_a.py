import re
from printf import printf
import copy

nodes = []

lines = 0
with open("22_input.txt") as f:
  for line in f:
    lines += 1
    if lines < 3:
      continue
    line_split = line.strip().split(' ')
    row = []
    for a in line_split:
      if a != '':
        a = a.replace('/dev/grid/node-', '')
        a = a.replace('T', '')
        a = a.replace('%', '')
        if a.isdigit():
          a = int(a)
        row.append(a)
    nodes.append(row)

viable_nodes = []

for a in nodes:
  for b in nodes:
    if a[0] == b[0]:
      continue
    pair_name = ''
    if a[0] < b[0]:
      pair_name = a[0] + '+' + b[0]
    else:
      pair_name = b[0] + '+' + a[0]
    if pair_name in viable_nodes:
      continue
    if a[2] == 0:
      continue
    if a[2] <= b[3]:
      viable_nodes.append(pair_name)

print len(viable_nodes)


      
