triangles = []
valid=0
with open("03_input.txt") as f:
  a_sides = []
  b_sides = []
  c_sides = []
  for line in f:
    side = line.strip().split()
    a = int(side[0])
    b = int(side[1])
    c = int(side[2])
    a_sides.append(a)
    b_sides.append(b)
    c_sides.append(c)
    if len(a_sides) == 3:
      triangles.append(a_sides)
      triangles.append(b_sides)
      triangles.append(c_sides)
      a_sides = []
      b_sides = []
      c_sides = []


valid = 0

for t in triangles:
    a = t[0]
    b = t[1]
    c = t[2]

    if a+b>c:
      if a+c>b:
        if b+c>a:
          valid += 1

print valid
