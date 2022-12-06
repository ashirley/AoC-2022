import sys, re

for line in sys.stdin:
  x = 4
  i = 0
  buf = []

  buf.append(line[0])
  buf.append(line[1])
  buf.append(line[2])
  buf.append(line[3])

  while len(set(buf)) != 4:
    print (x, line[x], buf, len(set(buf)))
    buf[i] = line[x]
    i += 1
    if i == 4:
      i = 0
    x += 1

  print(x)
