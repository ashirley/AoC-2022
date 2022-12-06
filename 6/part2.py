import sys, re

n=14

for line in sys.stdin:
  x = n
  i = 0
  buf = []

  #setup by copying the first n
  for j in range(n):
    buf.append(line[j])

  while len(set(buf)) != n:
    print (x, line[x], buf, len(set(buf)))
    buf[i] = line[x]
    i += 1
    if i == n:
      i = 0
    x += 1

  print(x)
